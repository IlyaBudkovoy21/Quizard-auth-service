from abc import ABC

from src.config.database import AsyncSession


class BaseAsyncService(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session
