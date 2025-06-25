from authx import AuthXConfig
from dotenv import load_dotenv


load_dotenv()

config = AuthXConfig()
config.JWT_SECRET_KEY = ""
