from app.models.user import User
from app.dtos.user_dto import UserDTO
from app.forms.UserRegisterForm import UserRegisterForm
from app.forms.UserUpdateForm import UserUpdateForm
from app.forms.UserLoginForm import UserLoginForm


class UserMapper:
    @staticmethod
    def entity_to_dto(entity: User) -> UserDTO:
        return UserDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, user: User) -> User:
        if isinstance(form, UserRegisterForm):
            user.useremail = form.useremail.data
            user.userpassword = form.userpassword.data
            user.username = form.username.data
            user.userdescription = form.userdescription.data

        elif isinstance(form, UserUpdateForm):
            user.useremail = form.useremail.data
            user.userdescription = form.userdescription.data

        elif isinstance(form, UserLoginForm):
            user.userpassword = form.userpassword.data
            user.username = form.username.data

        return user
