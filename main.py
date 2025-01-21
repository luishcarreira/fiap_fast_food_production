import os
import sys

# get the project path dynamically to avoid hardcoded path
project_path = os.path.abspath(os.path.join('.'))

# check the path is not already in sys.path, to avoid duplicates
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from src.application.api.startup import StartupApi

if __name__ == "__main__":
    if os.environ.get('APPLICATION') == 'api':
        StartupApi.initialize()