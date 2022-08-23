from flask import session

from app.dtos.user_dto import UserDTO
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from app.services.user_service import UserService


class AuthServiceImpl(AuthService):
    @inject
    def __init__(self, userService: UserService):
        super().__init__()
        self.__user_service = userService
        self.__current_user = UserDTO()

        if session.get('userid') is not None:
            self.__current_user = userService.find_one(session.get('userid'))

    def get_current_user(self) -> UserDTO:
        return self.__current_user

    def set_current_user(self, user):
        self.__current_user = self.__user_service.find_one(user['userid'])
