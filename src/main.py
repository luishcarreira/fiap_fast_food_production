import os

from src.application.api.startup import Startup as StartupApi
from src.application.queue.startup import Startup as StartupQueue

if __name__ == "__main__":
    application = os.environ.get('APPLICATION')

    if application == 'api':
        print("Iniciando a aplicação API...")
        StartupApi.initialize()
    elif application == 'queue':
        print("Iniciando os consumidores de fila...")
        StartupQueue.initialize()
    else:
        raise ValueError("APPLICATION deve ser 'api' ou 'queue'")