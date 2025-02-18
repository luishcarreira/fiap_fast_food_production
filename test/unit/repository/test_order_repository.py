import pytest
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime

from src.domain.entities.combo_entity import ComboEntity
from src.domain.entities.order_entity import OrderEntity
from src.domain.enums.order_status_enum import OrderStatusEnum
from src.domain.enums.production_status_enum import ProductionStatusEnum
from src.infra.models.combo_model import ComboModel
from src.infra.models.order_model import OrderModel
from src.infra.repositories.order_repository import OrderRepository


# Mocking a session factory for testing
@pytest.fixture(scope='function')  # Definindo explicitamente o escopo do loop assíncrono
def mock_session_factory():
    session_mock = AsyncMock()
    yield session_mock
    session_mock.reset_mock()

@pytest.mark.asyncio
async def test_get_order(mock_session_factory):
    order_id = 1
    # Mockando a execução do select
    order_model_mock = MagicMock(OrderModel)
    order_model_mock.id = order_id
    order_model_mock.status = OrderStatusEnum.RECEIVED
    order_model_mock.status_production = ProductionStatusEnum.PREPARANDO_LANCHE
    order_model_mock.start_time = datetime.now()
    order_model_mock.finished_time = None
    order_model_mock.combos = []

    # Criando um AsyncMock para simular o retorno de execute()
    mock_result = AsyncMock()
    mock_result.scalar_one_or_none = AsyncMock(return_value=order_model_mock)
    mock_session_factory.return_value.__aenter__.return_value.execute = AsyncMock(return_value=mock_result)

    order_repository = OrderRepository(mock_session_factory)
    order = await order_repository.get(order_id)

    assert order is not None
    assert order.id == order_id
    assert order.status == OrderStatusEnum.RECEIVED


# @pytest.mark.asyncio
# async def test_create_order(mock_session_factory):
#     # Criando mock para ComboModel
#     combo_model_mock = MagicMock(ComboModel)
#     combo_model_mock.id = 1
#     combo_model_mock.id_product = 1001
#     combo_model_mock.addons = []
#
#     # Mockando o comportamento do session.execute
#     mock_result = AsyncMock()
#     mock_result.scalar_one_or_none.return_value = combo_model_mock
#     mock_session_factory.return_value.__aenter__.return_value.execute.return_value = mock_result
#
#     # Criando o objeto OrderEntity para criar
#     order_entity = OrderEntity(
#         id=1,
#         status=OrderStatusEnum.RECEIVED,
#         start_time=datetime.now(),
#         finished_time=None,
#         combos=[ComboEntity(id=1, id_product=1001, addons=[])]
#     )
#
#     # Mockando a criação de OrderModel
#     order_model_mock = MagicMock(OrderModel)
#     order_model_mock.id = 1
#     order_model_mock.status = OrderStatusEnum.RECEIVED
#     order_model_mock.status_production = ProductionStatusEnum.PREPARANDO_LANCHE
#     order_model_mock.start_time = datetime.now()
#     order_model_mock.finished_time = None
#     order_model_mock.combos = [combo_model_mock]
#
#     mock_session_factory.return_value.__aenter__.return_value.add.return_value = None
#     mock_session_factory.return_value.__aenter__.return_value.commit.return_value = None
#
#     # Testando a criação do pedido
#     order_repository = OrderRepository(mock_session_factory)
#     created_order = await order_repository.create(order_entity)
#
#     assert created_order is not None
#     assert created_order.id == 1
#     assert created_order.status == OrderStatusEnum.RECEIVED

@pytest.mark.asyncio
async def test_update_status(mock_session_factory):
    order_id = 1
    status = ProductionStatusEnum.PREPARANDO_LANCHE

    # Mockando a execução do select
    order_model_mock = MagicMock(OrderModel)
    order_model_mock.id = order_id
    order_model_mock.status_production = status.value

    mock_result = AsyncMock()
    mock_result.scalar_one_or_none.return_value = order_model_mock
    mock_session_factory.return_value.__aenter__.return_value.execute.return_value = mock_result

    # Testando a atualização do status
    order_repository = OrderRepository(mock_session_factory)
    result = await order_repository.update_status(order_id, status)

    assert result is True
    order_model_mock.status_production = status


# Testando quando o pedido não é encontrado
@pytest.mark.asyncio
async def test_get_order_not_found(mock_session_factory):
    order_id = 999  # ID que não existe

    # Mockando o retorno do select para não encontrar nada
    mock_session_factory.return_value.__aenter__.return_value.execute.return_value.scalar_one_or_none.return_value = None

    order_repository = OrderRepository(mock_session_factory)
    order = await order_repository.get(order_id)

    assert order is None


# Testando quando o combo não é encontrado
# @pytest.mark.asyncio
# async def test_create_order_combo_not_found(mock_session_factory):
#     order_entity = OrderEntity(
#         id=1,
#         status=OrderStatusEnum.RECEIVED,
#         status_production=ProductionStatusEnum.PREPARANDO_LANCHE,
#         start_time=datetime.now(),
#         finished_time=None,
#         combos=[ComboEntity(id=999, id_product=1001, addons=[])]  # Combo com id que não existe
#     )
#
#     # Mockando o comportamento de ComboModel não encontrado
#     mock_session_factory.return_value.__aenter__.return_value.execute.return_value.scalar_one_or_none.return_value = None
#
#     order_repository = OrderRepository(mock_session_factory)
#
#     with pytest.raises(ValueError):
#         await order_repository.create(order_entity)
