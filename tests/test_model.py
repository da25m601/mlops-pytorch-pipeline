import torch

from src.model import create_model


def test_model_output_shape():
    model = create_model(num_classes=10)

    inputs = torch.randn(2, 3, 32, 32)
    outputs = model(inputs)

    assert outputs.shape == (2, 10)
