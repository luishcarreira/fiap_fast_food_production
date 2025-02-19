# My Python Project

This project is a Python-based application that includes various functionalities such as order creation, combo management, and integration with a message queue.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker](#docker)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/luishcarreira/my-python-project.git
    cd my-python-project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

The application provides the following API endpoints:
- `/api/production/add_order`: Adds a new order to the queue.
- `/api/production/update_status/{id_order}`: Updates an existing order in the queue.

## Docker

To build and run the Docker container, use the following command:
```sh
docker build -t my-python-project .
docker run -p 8000:8000 my-python-project
```