import FlaskWebProject.views
import logging
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Enable logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
