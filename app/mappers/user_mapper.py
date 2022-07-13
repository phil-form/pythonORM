from app.mappers.abstract_mapper import AbstractMapper
from app.models.user import User
from app.dtos.user_dto import UserDTO
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_update_form import UserUpdateForm
from app.forms.user.user_login_form import UserLoginForm


class UserMapper(AbstractMapper):
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

            if form.userroles.data is not []:
                form.manage_roles(user)

        elif isinstance(form, UserLoginForm):
            user.userpassword = form.userpassword.data
            user.username = form.username.data

        return user
