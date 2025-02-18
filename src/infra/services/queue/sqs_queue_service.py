import os
from typing import List

import boto3
import inject
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

from src.domain.interfaces.services.queue.i_queue_service import IQueueService


class AwsSqsQueueService(IQueueService):
    inject.autoparams()

    def __init__(self):
        load_dotenv()

        self._aws_region = os.getenv("AWS_REGION", "us-east-1")
        self._aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self._aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self._aws_session_token = os.getenv("AWS_SESSION_TOKEN")
        self._sqs_queue_url = os.getenv("SQS_QUEUE_URL")
        self._queue_name = os.getenv("QUEUE_NAME")

        self.sqs_client = boto3.client(
            service_name="sqs",
            region_name=self._aws_region,
            aws_access_key_id=self._aws_access_key_id,
            aws_secret_access_key=self._aws_secret_access_key,
            aws_session_token=self._aws_session_token,
            endpoint_url=self._sqs_queue_url,
        )

    async def send_message(self, message: str, delay_seconds: int = 0) -> None:
        try:
            queue_url = self.sqs_client.get_queue_url(QueueName=self._queue_name)["QueueUrl"]
            self.sqs_client.send_message(
                QueueUrl=queue_url,
                MessageBody=message,
                DelaySeconds=delay_seconds,
            )
        except Exception as e:
            raise RuntimeError(f"Erro ao enviar mensagem para a fila {self._queue_name}: {str(e)}")

    async def receive_messages(self, max_messages: int = 10) -> List[str]:
        try:
            queue_url = self.sqs_client.get_queue_url(QueueName=self._queue_name)["QueueUrl"]
            response = self.sqs_client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=max_messages,
                WaitTimeSeconds=10
            )
            return [msg["Body"] for msg in response.get("Messages", [])]
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Erro ao receber mensagens: {e}")
