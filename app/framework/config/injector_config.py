from app.framework.injector import ContainerConfig, DependencyConfig, Scope
from app.services.auth_service import AuthService
from app.services.auth_service_impl import AuthServiceImpl
from app.services.basket_service import BasketService
from app.services.item_service import ItemService
from app.services.role_service import RoleService
from app.services.user_service import UserService


def config_injector(config: ContainerConfig):
    config.bind(DependencyConfig(UserService, UserService, Scope.SINGLETON))
    config.bind(DependencyConfig(RoleService, RoleService, Scope.SINGLETON))
    config.bind(DependencyConfig(BasketService, BasketService, Scope.SINGLETON))
    config.bind(DependencyConfig(ItemService, ItemService, Scope.SINGLETON))
    config.bind(DependencyConfig(AuthService, AuthServiceImpl, Scope.SCOPED))
