import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """
    Application configuration settings.
    """
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'default_user')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'host.docker.internal')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'quakedb')

    # Construct the SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy's event notifications to save resource