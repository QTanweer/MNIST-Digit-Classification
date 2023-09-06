# README

## Overview

This is an image classification project using the MNIST dataset with PyTorch, Docker and GitHub Actions.

The project contains:

- `models/mnist_model.py` - The PyTorch model definition
- `notebooks/train.ipynb` - Notebook to train the model
- `app/app.py` - Flask app to serve predictions
- Dockerfile and docker-compose.yml to containerize the app
- `.github/workflows/main.yml` - CI/CD workflow with GitHub Actions

## Running the app

To run the Docker containers:
  docker-compose up --build


The app will be served at `http://localhost:5000`

Jupyter notebook can be accessed at `http://localhost:8888` 

To retrain the model, run `train.ipynb`, then rebuild the Docker image.

## CI/CD Pipeline 

The GitHub Actions workflow trains the model on new code changes, evaluates it, and automatically deploys the Docker image.

Workflow runs can be seen under the Actions tab.