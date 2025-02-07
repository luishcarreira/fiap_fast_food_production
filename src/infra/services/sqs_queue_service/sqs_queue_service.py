from typing import List

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from settings import get_settings

from src.domain.interfaces.services.queue.i_queue_service import IQueueService


class AwsSqsQueueService(IQueueService):
    def __init__(self):
        settings = get_settings()

        self.sqs_client = boto3.client(
            service_name="sqs",
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            aws_session_token=settings.aws_session_token,
            endpoint_url=settings.sqs_queue_url,
        )

    async def send_message(self, queue_name: str, message: str, delay_seconds: int = 0) -> None:
        try:
            queue_url = self.sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]
            self.sqs_client.send_message(
                QueueUrl=queue_url,
                MessageBody=message,
                DelaySeconds=delay_seconds,
            )
        except Exception as e:
            raise RuntimeError(f"Erro ao enviar mensagem para a fila {queue_name}: {str(e)}")

    async def receive_messages(self, queue_name: str, max_messages: int = 10) -> List[str]:
        try:
            queue_url = self.sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]
            response = self.sqs_client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=max_messages,
                WaitTimeSeconds=10
            )
            return [msg["Body"] for msg in response.get("Messages", [])]
        except (BotoCoreError, ClientError) as e:
            raise RuntimeError(f"Erro ao receber mensagens: {e}")
