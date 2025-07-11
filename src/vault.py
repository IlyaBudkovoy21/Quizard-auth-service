import os
from dotenv import load_dotenv
from hvac import Client
from typing import Optional

load_dotenv()


class HvacClient:
    def __init__(self, url: Optional[str] = None, token: Optional[str] = None):
        self._vault_url = url or os.getenv("VAULT_URL")
        self._vault_token = token or os.getenv("VAULT_TOKEN")

        if not self._vault_url:
            raise ValueError("Url is not specified")
        if not self._vault_token:
            raise ValueError("Token is not specified")
        self.create_client()

    def create_client(self):
        self.client = Client(url=self._vault_url, token=self._vault_token)

    def read_item(self, mount_point: str, path: str, key: str) -> str:
        secret_key = self.client.secrets.kv.v1.read_secret(
            path=path, mount_point=mount_point
        )
        return secret_key["data"]["data"][key]

    def read_db_secret(self, key: str):
        return self.read_item(mount_point="kv/", path="database_info", key=key)


hvac_client = HvacClient()
