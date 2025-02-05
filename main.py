import os
from src.application.api.startup import StartupApi

if __name__ == "__main__":
    if os.environ.get('APPLICATION') == 'api':
        StartupApi.initialize()