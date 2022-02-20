import pytest
from delivery.app import create_app

@pytest.fixture(scope="module")
def app():
    """Teste"""
    return create_app()