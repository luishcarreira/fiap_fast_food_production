from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    python_env: str
    application: str
    consumer: str
    queue_name: str

    # postgresql
    postgresql_host: str
    postgresql_username: str
    postgresql_password: str
    postgresql_database: str
    postgresql_port: int

    # aws
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_session_token: str
    aws_region: str
    sqs_queue_url: str

    # order service
    order_service_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
