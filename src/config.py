from authx import AuthXConfig
from dotenv import load_dotenv
from src.vault import hvac_client

load_dotenv()

config = AuthXConfig()
config.JWT_SECRET_KEY = hvac_client.read_item(path="jwt", mount_point="kv/data", key="JWT_SECRET_KEY")
