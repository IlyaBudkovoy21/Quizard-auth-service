import pytest

from src.vault import HvacClient


class TestInit:
    def test_init_with_params(self):
        """Инициализация с прямым указанием параметров"""
        client = HvacClient(url="http://test", token="test")
        assert client._vault_url == "http://test"
        assert client._vault_token == "test"

    def test_init_with_env(self, monkeypatch):
        """Инициализация через переменные окружения"""
        monkeypatch.setenv("VAULT_URL", "http://env")
        monkeypatch.setenv("VAULT_TOKEN", "env_token")
        client = HvacClient()
        assert client._vault_url == "http://env"
        assert client._vault_token == "env_token"

    def test_init_missing_url(self, monkeypatch):
        """Проверка ошибки при отсутствии URL"""
        monkeypatch.delenv("VAULT_URL")
        with pytest.raises(ValueError, match="Url is not specified"):
            HvacClient(token="test")

    def test_init_missing_token(self, monkeypatch):
        """Проверка ошибки при отсутствии токена"""
        monkeypatch.delenv("VAULT_TOKEN")
        with pytest.raises(ValueError, match="Token is not specified"):
            HvacClient(url="http://test")
