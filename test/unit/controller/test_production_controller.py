import os

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.application.test.startup import Startup as StartupTest
from src.domain.enums.production_status_enum import ProductionStatusEnum


@pytest.fixture
def client():
    os.environ['APPLICATION'] = 'test'

    app = StartupTest.initialize()

    return TestClient(app)

# Teste para o endpoint de adicionar pedido
@patch('src.domain.usecases.order.send_order_to_queue_uc.SendOrderToQueueUC.execute')
def test_add_order_success(mock_execute, client):
    # Simulando um sucesso na execução do caso de uso
    mock_execute.return_value = None  # Nenhum retorno, apenas sucesso

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

    response = client.post("/api/production/add_order", json=payload)

    assert response.status_code == 201
    assert response.json() == {"message": "Order added successfully"}

@patch('src.domain.usecases.order.send_order_to_queue_uc.SendOrderToQueueUC.execute')
def test_add_order_failure(mock_execute, client):
    # Simulando um erro ao executar o caso de uso
    mock_execute.side_effect = Exception("Queue service error")

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

    response = client.post("/api/production/add_order", json=payload)

    assert response.status_code == 500
    assert response.json() == {"detail": "Error adding order to queue: Queue service error"}

# Teste para o endpoint de atualizar status do pedido
@patch('src.domain.usecases.order.order_update_status_uc.OrderUpdateStatusUC.execute')
def test_update_status_success(mock_execute, client):
    # Simulando um sucesso na execução do caso de uso
    mock_execute.return_value = None  # Nenhum retorno, apenas sucesso

    id_order = 1
    status = ProductionStatusEnum.PREPARANDO_LANCHE.value

    response = client.patch(f"/api/production/update_status/{id_order}?status={status}")

    assert response.status_code == 200
    assert response.json() == {"message": "Order updated successfully"}

@patch('src.domain.usecases.order.order_update_status_uc.OrderUpdateStatusUC.execute')
def test_update_status_failure(mock_execute, client):
    # Simulando um erro ao executar o caso de uso
    mock_execute.side_effect = Exception("Update status failed")

    id_order = 1
    status = ProductionStatusEnum.PREPARANDO_LANCHE.value

    response = client.patch(f"/api/production/update_status/{id_order}?status={status}")

    assert response.status_code == 500
    assert response.json() == {"detail": "Error updating order status: Update status failed"}
