


```
ML Project Template
This repository provides a complete machine learning project template with a modular codebase, 
configuration-driven design, and built-in support for Docker, CI/CD, and web interfaces.
```
```text
📁 Project Structure

 
.
├── app.py                 # Web or API interface (e.g., FastAPI/Flask)
├── main.py                # Entry point for running the ML pipeline
├── setup.py               # Packaging and installation
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container setup
├── LICENSE                # MIT License for open-source use
├── README.md              # Project overview and instructions
├── params.yaml            # Hyperparameters/config for ML experiments
├── schema.yaml            # Data schema definitions
├── test.py                # Test script (currently empty)
│
├── .github/               # GitHub Actions workflows for CI/CD
│
├── config/
│   └── config.yaml        # Application configuration
│
├── logs/
│   └── running_logs.log   # Execution logs
│
├── research/
│   └── trials.ipynb       # Jupyter notebooks for experimentation
│
├── templates/
│   └── index.html         # Web interface templates
│
└── src/
    └── mlProject/
        ├── __init__.py           # Package initializer + logging setup
        ├── components/           # ML pipeline components
        ├── config/               # Configuration management (e.g., configuration.py)
        ├── constants/            # Project-wide constants
        ├── entity/               # Data and config entity definitions
        ├── pipeline/             # ML pipeline orchestration
        ├── utils/                # Utility functions (e.g., common.py)
        └── template.py           # Script to auto-generate project structure



## Workflows

1. Update config.yaml    # Stores configuration details for your project, such as paths, settings, or environment variables.
2. Update schema.yaml
3. Update params.yaml
4. Update the entity # return type of a function
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py
```
# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/mayank61/MLops_basics_project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='mayank61', repo_name='MLops_basics_project', mlflow=True)


```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model



