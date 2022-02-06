from services.base_service import BaseService
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'backend.env'
load_dotenv(dotenv_path=env_path)


import controllers
from controllers import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
