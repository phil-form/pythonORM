from app import app
import os

from app.framework.config.injector_config import config_injector
from app.framework.injector import Injector

port = int(os.environ.get('PORT', 8080))
injector = Injector(app, config=config_injector)

app.run('0.0.0.0', port=port)
