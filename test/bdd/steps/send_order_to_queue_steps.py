import asyncio
import json
import os

import inject
from behave import given, when, then
from behave.api.async_step import async_run_until_complete
from starlette.testclient import TestClient

from src.application.test.startup import Startup as StartupTest
from src.domain.interfaces.services.queue.i_queue_service import IQueueService


@given("the API is running")
def step_api_is_running(context):
    os.environ['APPLICATION'] = 'test'

    app = StartupTest.initialize()

    context.client = TestClient(app)


@given("the order queue is empty")
def step_queue_is_empty(context):
    """Limpa a fila de mensagens antes de realizar o teste"""
    context.mock_queue_service = inject.instance(IQueueService)
    context.mock_queue_service().clear_queue()
    assert len(context.mock_queue_service.sent_messages) == 0


@when("an order is sent to the API with valid data")
@async_run_until_complete(timeout=1.2)
async def step_send_order_to_api(context):
    """Envia uma ordem para a API com dados válidos"""
    payload = {
        "id": 1,
        "combos": [
            {
                "id": 101,
                "product": {
                    "id": 201,
                    "name": "Combo Jantinha",
                    "description": "1 espetinho de carne, arroz, vinagrete, mandioca e farofa.",
                    "estimated_time": 20,
                    "product_category": "Lanche"
                },
                "addons": [
                    {
                        "id": 301,
                        "name": "Espetinho de Frango",
                        "product_category": "Lanche"
                    },
                    {
                        "id": 302,
                        "name": "Porção de Batata Frita",
                        "product_category": "Acompanhamento"
                    }
                ]
            },
            {
                "id": 102,
                "product": {
                    "id": 202,
                    "name": "Combo 1",
                    "description": "4 espetinhos de sua escolha, arroz, vinagrete, mandioca e farofa.",
                    "estimated_time": 30,
                    "product_category": "Lanche"
                },
                "addons": [
                    {
                        "id": 303,
                        "name": "Espetinho de Linguiça",
                        "product_category": "Lanche"
                    },
                    {
                        "id": 304,
                        "name": "Refrigerante Lata",
                        "product_category": "Bebida"
                    }
                ]
            }
        ]
    }

    # Envia a ordem para a API e aguarda a resposta
    response = context.client.post("/api/production/add_order", json=payload)
    context.response = response


@then("the response status should be 201")
def step_check_response_status(context):
    """Verifica se a resposta da API foi bem-sucedida com status 201"""
    assert context.response.status_code == 201


@then("the order should be sent to the production queue")
def step_order_sent_to_queue(context):
    """Verifica se a ordem foi enviada para a fila de produção"""
    print("Messages sent so far:", context.mock_queue_service.sent_messages)
    assert len(context.mock_queue_service.sent_messages) == 1, "Expected the order to be in the queue."

    # Verifica o conteúdo da ordem enviada
    order_message = json.loads(context.mock_queue_service.sent_messages[0])
    assert order_message['id'] == 1, f"Expected order ID 1, but got {order_message['id']}"
