from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase

from src.vault import hvac_client


database_url = URL(
    "postgres+psycopg2",
    host=hvac_client.read_db_secret(key="host"),
    username=hvac_client.read_db_secret(key="username"),
    password=hvac_client.read_db_secret(key="password"),
    port=hvac_client.read_db_secret(key="port"),
    database=hvac_client.read_db_secret(key="database"),
    query=dict(),
)


db_engine = create_engine(database_url)


class Base(DeclarativeBase):
    pass
