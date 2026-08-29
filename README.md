# MLOps PyTorch Pipeline

## Overview

This project implements an end-to-end MLOps pipeline for deploying a PyTorch image classification workload.

The project covers the complete deployment lifecycle:

* Git-based development and collaboration
* PyTorch model training
* Docker-based containerization
* Kubernetes-based training and model serving
* Health checks and prediction APIs
* Configuration management using ConfigMaps and Secrets
* End-to-end validation

The project is developed locally and the Docker and Kubernetes workloads are executed on a server-based environment.

## Project Objectives

The main objectives of this project are to:

1. Structure an ML project using proper Git workflows.
2. Implement a PyTorch image classification model.
3. Containerize training and model serving using Docker.
4. Run model training as a Kubernetes Job.
5. Deploy the trained model using a Kubernetes Deployment.
6. Expose the model through a Kubernetes Service.
7. Validate the complete training-to-serving workflow.

## Technology Stack

* Python
* PyTorch
* torchvision
* Docker
* Kubernetes
* kubectl
* Git
* GitHub
* GitHub Actions
* FastAPI
* YAML

## Repository Structure

```text
mlops-pytorch-pipeline/
│
├── README.md
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── train.py
│   ├── model.py
│   ├── dataset.py
│   └── serve.py
│
├── configs/
│   └── training_config.yaml
│
├── docker/
│   ├── Dockerfile.train
│   └── Dockerfile.serve
│
├── k8s/
│   ├── namespace.yaml
│   ├── training-job.yaml
│   ├── serving-deployment.yaml
│   ├── serving-service.yaml
│   ├── configmap.yaml
│   ├── pvc.yaml
│   └── hpa.yaml
│
├── requirements/
│   ├── train.txt
│   └── serve.txt
│
└── tests/
    └── test_model.py
```

## Development Workflow

Development follows a feature-branch Git workflow.

```text
main
  │
  └── develop
        │
        ├── feature/project-setup
        ├── feature/pytorch-model
        ├── feature/docker
        └── feature/kubernetes
```

All feature work is developed on feature branches and merged through Pull Requests.

The final completed work is merged into the `main` branch through a Pull Request.

## Architecture

The project follows a staged MLOps workflow:

```text
Developer
    │
    ▼
GitHub Repository
    │
    ├──────────────► PyTorch Model
    │                     │
    │                     ▼
    │                Training Code
    │                     │
    │                     ▼
    │              Docker Training Image
    │                     │
    │                     ▼
    │              Training Container
    │                     │
    │                     ▼
    │              Model Checkpoint
    │                     │
    │                     ▼
    │              Docker Serving Image
    │                     │
    │                     ▼
    │              FastAPI Serving
    │                 │          │
    │                 ▼          ▼
    │              /health    /predict
    │
    └──────────────► Optional Kubernetes Components
                          │
                          ├── Training Job
                          ├── Persistent Storage
                          ├── Model Serving
                          └── Service / HPA

```

The Docker-based training and serving workflow was successfully implemented
and validated.

The Kubernetes components were implemented as optional deployment artifacts.
End-to-end Kubernetes execution could not be completed because the designated
course server encountered a disk-space limitation.
```

## Local Development

The source code and project configuration are maintained using VS Code and Git.

Create and activate a Python virtual environment before working with the
project.

```bash
python -m venv .venv
.venv\Scripts\activate

```

Install the training dependencies:

```bash
pip install -r requirements/train.txt
```
For serving development, install:

```bash
pip install -r requirements/serve.txt
```


## Docker

The project provides separate Docker images for:

- Model training
- Model serving

### Training Image

Build the training image from the repository root:

```bash
docker build -f docker/Dockerfile.train -t mlops-train:v1 .
```
Run the training workload with the data and checkpoint directories mounted:

```bash
docker run --rm \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/checkpoints:/app/checkpoints" \
  mlops-train:v1
```
The training container reads its configuration from:
/app/configs/training_config.yaml

The trained model checkpoint is saved under:
/app/checkpoints

### Serving Image

Build the serving image:
```bash
docker build -f docker/Dockerfile.serve -t mlops-serve:v1 .
```

Run the serving container:
```bash
docker run --rm \
  -p 8080:8080 \
  -v "$(pwd)/checkpoints:/app/checkpoints:ro" \
  mlops-serve:v1
```

### Health Check

The serving application exposes: GET /health

A successful response indicates that the model has been loaded correctly.

### Prediction

The serving application exposes: POST /predict

### Example Request

```bash
curl -X POST http://localhost:8080/predict \
  -F "image=@test_image.png"
```


## Kubernetes

Kubernetes deployment components are included as an optional extension to the
Docker-based MLOps pipeline.

The Kubernetes manifests consist of:

- A dedicated namespace
- Configuration management using a ConfigMap
- PersistentVolumeClaims for training data and model checkpoints
- A Kubernetes Training Job
- A model-serving Deployment
- A Kubernetes Service
- Health checks
- Horizontal Pod Autoscaling

### Kubernetes Deployment Status

The Kubernetes manifests were implemented and their YAML syntax was validated.

The Kubernetes deployment could not be completed end-to-end because the
designated course server encountered a disk-space limitation. The server
filesystem reached 100% utilization during the Minikube/Kubernetes setup,
which prevented reliable execution of the Kubernetes workloads.

The PersistentVolumeClaims were subsequently created successfully and reached
the `Bound` state. However, the Kubernetes Training Job could not be completed
because of the server-side resource/storage limitations.

Therefore, the repository does not claim successful end-to-end Kubernetes
validation.

The Docker-based training and model-serving workflow was successfully
implemented and validated.

## Validation

The implemented workflow was validated through:

1. Local application testing
2. Docker training image build
3. Docker training execution
4. Model checkpoint generation
5. Docker serving image build
6. Serving container startup
7. Health-check validation
8. Prediction API testing

The Docker-based training and model-serving workflow was successfully
validated.

The Kubernetes deployment components were implemented as an optional
extension, but end-to-end Kubernetes validation could not be completed because
of the disk-space limitation on the designated course server.

Validation evidence for the completed Docker workflow is documented in the
Pull Request.


## Submission

This repository is developed as part of the MLOps & Infrastructure for Machine Learning course assignment.

The final submission will include:

* GitHub repository
* Merged Pull Requests
* Validation screenshots/terminal output
* Final project documentation
* Reflection on the implementation challenges
