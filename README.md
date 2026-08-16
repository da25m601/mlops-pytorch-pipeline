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

The architecture diagram will be added after the implementation and deployment architecture have been finalized.

## Local Development

The source code and project configuration are maintained on the development laptop using VS Code and Git.

Docker image builds and Kubernetes deployment are performed on the designated server environment.

Detailed setup and execution instructions will be added as the individual components are implemented.

## Docker

The project provides separate Docker images for:

* Model training
* Model serving

Detailed Docker build and execution instructions will be added during the containerization phase.

## Kubernetes

The Kubernetes deployment consists of:

* A dedicated namespace
* Configuration management
* A training Job
* Persistent storage for data and model checkpoints
* A model-serving Deployment
* A Kubernetes Service
* Health checks
* Horizontal Pod Autoscaling

Detailed Kubernetes deployment and validation instructions will be added during the Kubernetes implementation phase.

## Validation

The complete workflow will be validated through:

1. Local application testing
2. Docker training and serving tests
3. Kubernetes training Job execution
4. Kubernetes serving deployment
5. Health-check validation
6. Prediction API testing

Validation evidence will be documented in the final Pull Request.

## Submission

This repository is developed as part of the MLOps & Infrastructure for Machine Learning course assignment.

The final submission will include:

* GitHub repository
* Merged Pull Requests
* Validation screenshots/terminal output
* Final project documentation
* Reflection on the implementation challenges
