import torch.nn as nn
from torchvision.models import resnet18


def create_model(num_classes: int = 10) -> nn.Module:
    """
    Create a ResNet-18 model configured for CIFAR-10 classification.
    """
    model = resnet18(weights=None)

    # CIFAR-10 images are 32x32, so use a smaller
    # initial convolution and remove the initial max-pooling layer.
    model.conv1 = nn.Conv2d(
        in_channels=3,
        out_channels=64,
        kernel_size=3,
        stride=1,
        padding=1,
        bias=False,
    )

    model.maxpool = nn.Identity()

    # Replace the final classification layer.
    model.fc = nn.Linear(model.fc.in_features, num_classes)

    return model
