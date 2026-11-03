import os
from dotenv import load_dotenv

# Load configuration from the project's .env file.
load_dotenv()

# Application configuration.
APP_NAME = os.getenv("APP_NAME","ShopEase Product Service",)

APP_VERSION = os.getenv("APP_VERSION","1.0.0",)

APP_HOST = os.getenv("APP_HOST","0.0.0.0",)

APP_PORT = int(os.getenv("APP_PORT", "8003"))

DEBUG = os.getenv("DEBUG","false",).lower() in {"true", "1", "yes"}