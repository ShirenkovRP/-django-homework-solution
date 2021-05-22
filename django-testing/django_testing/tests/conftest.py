import pytest
from rest_framework.test import APIClient


#  Создаем расширенного тестового клиента (фиктивный браузер)
@pytest.fixture
def api_client():
    return APIClient()
