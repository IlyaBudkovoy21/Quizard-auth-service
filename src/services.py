from src.schemas import UserRegistrationData
from src.base import BaseAsyncService


class UserService(BaseAsyncService):
    def create_user(self, user_data: UserRegistrationData):
        pass
