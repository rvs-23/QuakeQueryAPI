import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.config import Config

@pytest.fixture
def engine():
    """
    Pytest fixture to create and provide a SQLAlchemy engine.
    """
    return create_engine(Config.SQLALCHEMY_DATABASE_URI)

def test_connection(engine):
    """
    Test the database connection using the provided configuration.
    """
    print(f"Connecting to database using URI: {Config.SQLALCHEMY_DATABASE_URI}")
    try:
        connection = engine.connect()
        assert connection is not None, "Failed to establish a database connection."
        print("Connection successful!")
    except OperationalError as e:
        pytest.fail(f"Connection failed: {e}")
    finally:
        connection.close()