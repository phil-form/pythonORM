from app.dtos.basket_dto import BasketDTO
from app.models.basket import Basket


class BasketMapper:
    @staticmethod
    def entity_to_dto(entity: Basket) -> BasketDTO:
        return BasketDTO.build_from_entity(entity)

    # @staticmethod
    # def form_to_entity(form, basket: Basket) -> Basket:
    #     if isinstance(form, ):
    #         user.useremail = form.useremail.data
    #         user.userpassword = form.userpassword.data
    #         user.username = form.username.data
    #         user.userdescription = form.userdescription.data
    #
    #     elif isinstance(form, UserUpdateForm):
    #         user.useremail = form.useremail.data
    #         user.userdescription = form.userdescription.data
    #
    #     elif isinstance(form, UserLoginForm):
    #         user.userpassword = form.userpassword.data
    #         user.username = form.username.data
    #
    #     return user
