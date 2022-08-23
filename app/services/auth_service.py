from abc import ABC, abstractmethod

from app.dtos.user_dto import UserDTO


class AuthService(ABC):
    def __init__(self):
        print("INIT AUTH SERVICE")

    def __del__(self):
        print("DELETE AUTH SERVICE")

    @abstractmethod
    def get_current_user(self) -> UserDTO:
        pass

    def set_current_user(self, user):
        pass