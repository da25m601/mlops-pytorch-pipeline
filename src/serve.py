import io
import os
from pathlib import Path

import torch
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image

from src.model import create_model


# CHECKPOINT_PATH = Path("checkpoints/classifier_v1.pt")
CHECKPOINT_PATH = Path(
    os.environ.get("CHECKPOINT_PATH", "checkpoints/classifier_v1.pt")
)
app = FastAPI(title="MLOps PyTorch Classifier")

model = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model() -> None:
    global model

    if not CHECKPOINT_PATH.exists():
        return

    model = create_model(num_classes=10)

    checkpoint = torch.load(
        CHECKPOINT_PATH,
        map_location=device,
    )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()


@app.on_event("startup")
def startup_event() -> None:
    load_model()


@app.get("/health")
def health() -> dict:
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded",
        )

    return {"status": "ok"}


@app.post("/predict")
async def predict(image: UploadFile = File(...)) -> dict:
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model is not loaded",
        )

    try:
        image_bytes = await image.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        image = image.resize((32, 32))

        image_tensor = torch.tensor(
            list(image.getdata()),
            dtype=torch.float32,
        ).reshape(32, 32, 3)

        image_tensor = image_tensor.permute(2, 0, 1) / 255.0

        mean = torch.tensor([0.4914, 0.4822, 0.4465]).view(3, 1, 1)
        std = torch.tensor([0.2470, 0.2435, 0.2616]).view(3, 1, 1)

        image_tensor = (image_tensor - mean) / std
        image_tensor = image_tensor.unsqueeze(0).to(device)

        with torch.no_grad():
            logits = model(image_tensor)
            probabilities = torch.softmax(logits, dim=1)

        """
        probabilities = probabilities[0].cpu().tolist()

        return {
            "probabilities": probabilities,
            "predicted_class": int(torch.argmax(probabilities).item()),
        }
        """
        probabilities = probabilities[0].cpu()

        predicted_class = int(torch.argmax(probabilities).item())

        return {
            "probabilities": probabilities.tolist(),
            "predicted_class": predicted_class,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Unable to process image: {exc}",
        ) from exc
