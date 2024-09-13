This repository provides a template for creating and deploying a FastAPI project. Follow the steps below to set up the local environment, run the project, manage database migrations.

## Table of Contents

- [Features](#features)
- [Getting started](#getting-started)
   - [Initialize & Setup Environment](#1-initialize--setup-environment)
   - [Variables Configuration](#2-variables-configuration)
   - [Database Migrations](#3-database-migrations)
   - [Run the Project](#6-run-the-project)
- [Advanced Usage](#advanced-usage)
   - [Additional Useful scripts](#additional-useful-scripts)

### Features

- Python 3.11+ support
- SQLAlchemy 2.0+ support
- Asynchronous capabilities
- Database migrations using Alembic
- Basic Authentication using JWT
- Feature flagging to enable/disable features
- Readily available CRUD operations
- Type checking using mypy
- Linting using flake8
- Formatting using black
- Code quality analysis using SonarQube

### Getting Started

#### Requirements:
- Python 3
- Docker
- Postgres SQL

#### 1. Initialize & Setup Environment

- To initialize and set up your environment, run the following script:

```shell
./scripts/initialize-env.sh
```

This script installs the necessary dependencies and prepares the environment for running the FastAPI application on your machine.

##### Activate the environment

- To activate the python environment, run the following command:
```
# Mac & Linux:
source ./venv/bin/activate

# Windows
.\venv\scripts\activate
```

#### 2. Variables Configuration
Update database environment variables in your .env.local file:
```
DB_NAME=
DB_HOSTNAME=localhost
DB_PORT=3306
DB_USERNAME=
DB_PASSWORD=
```
Additional Configuration (Optional):
```
DB_ROOT_PASSWORD=
```

#### 3. Database Migrations
Create new database migrations when you make changes to your models. Use the following command:
```shell
alembic revision -m 'brief description of changes'
```

This command initializes a new migration script based on the changes made to your models. Provide a brief description of the changes in the migration message.

Apply the database migrations with the following command:
```shell
alembic upgrade head
```
This command updates the database schema to reflect the latest changes defined in the migration scripts

#### 6. Run the Project

##### Running Application Locally

```shell
./scripts/local_server.sh
```

This script upgrades the database migrations using Alembic and starts the FastAPI server using Uvicorn. The server is hosted on 0.0.0.0 and port 8000, making it accessible locally.

##### Running Application into Docker Container

- Create a file .env.docker with reference of .env.example
- Inject Docker environment using
  ```shell
  set -a source .env.docker set +a
- Execute following command to turn on the application
  ```shell
  docker compose --env-file .env.docker up
  ```

### Advanced Usage

#### Additional Useful scripts
- Tests - scripts/run_tests.sh
- Linting & Formatting - scripts/lint_and_format.sh
