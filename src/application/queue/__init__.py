import os
import importlib
import inspect
from pathlib import Path

from inject import instance

from src.domain.interfaces.services.queue.i_queue_handler import IQueueHandler
from src.domain.interfaces.services.queue.i_queue_service import IQueueService


async def start_consumer():
    # Obter as variáveis de ambiente
    consumer_name = os.getenv("CONSUMER")

    if not consumer_name:
        raise ValueError("A variável de ambiente 'CONSUMER' não está configurada.")

    # Caminho base para os consumidores
    consumers_dir = Path(__file__).parent / "consumers"

    # Procurar o arquivo correspondente
    for module_path in consumers_dir.glob("*.py"):
        module_name = module_path.stem  # Nome do arquivo sem extensão
        class_name = "".join(word.capitalize() for word in module_name.split("_"))  # CamelCase

        if class_name == consumer_name:
            # Carregar o módulo dinamicamente
            module = importlib.import_module(f"application.queue.consumers.{module_name}")

            # Procurar a classe no módulo
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if name == consumer_name and issubclass(cls, IQueueHandler):
                    # Resolver dependências do consumidor
                    consumer_instance = instance(cls)

                    # Resolver dependências do serviço de fila
                    queue_service = instance(IQueueService)

                    # Iniciar o loop de consumo
                    await start_consumer_loop(queue_service, consumer_instance)
                    return

    raise ValueError(f"Consumidor '{consumer_name}' não encontrado.")


async def start_consumer_loop(queue_service: IQueueService, handler: IQueueHandler):
    while True:
        try:
            # Receber mensagens da fila
            messages = await queue_service.receive_messages()
            if not messages:
                continue

            for raw_message in messages:
                try:
                    # Processar a mensagem com o handler
                    await handler.handle_message(raw_message)
                except Exception as e:
                    print(f"Erro ao processar mensagem: {e}")
        except Exception as e:
            print(f"Erro ao consumir mensagens da fila': {e}")
