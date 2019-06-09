"""Settings configuration - Configuration for environment variables can go in here."""

import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
API_URL = os.getenv('API_URL')
REGION_NAME = os.getenv('REGION_NAME')
PROFILE_NAME = os.getenv('PROFILE_NAME')
