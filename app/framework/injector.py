from enum import Enum

from flask import Flask, session, request


class Scope(Enum):
    # il n'existe qu'une instance dans l'application
    SINGLETON = 1
    # une instance par requête.
    SCOPED = 2
    # chaque appel crée une nouvelle instance.
    TRANSIENT = 3

class DependencyConfig:
    def __init__(self, base, implement, scope: Scope):
        self.base = base
        self.implement = implement
        self.scope = scope

class ContainerConfig:
    def __init__(self):
        self.__config = {}

    def bind(self, dependency: DependencyConfig):
        self.__config[dependency.base.__name__] = dependency

    def get(self, dep_name) -> DependencyConfig:
        return self.__config.get(dep_name)

class Injector:
    def __init__(self, app: Flask, config):
        print("INIT INJECTOR")
        self.__config = ContainerConfig()
        config(self.__config)
        app.injector = self
        self.__singleton = {}
        self.__scoped = {}

        app.before_request(self.__request_start)
        app.after_request(self.__request_end)

    def __get_session_id(self):
        for cookie, value in request.cookies.items():
            if cookie == 'session':
                return value

    def __request_start(self, *args, **kwargs):
        # print("START SCOPED")
        # print(session.get('csrf_token'))
        sessionid = self.__get_session_id()
        self.__scoped[sessionid] = {}

    def __request_end(self, response):
        # print("SCOPE END")
        sessionid = self.__get_session_id()
        self.__scoped[sessionid] = {}
        return response

    def __del__(self):
        print("DESTROY INJECTOR")

    def __getitem__(self, item):
        dep = self.__config.get(item)

        if dep is not None:
            if dep.scope.value == Scope.SCOPED.value:
                return self.__get_scoped(dep)
            elif dep.scope.value == Scope.SINGLETON.value:
                return self.__get_singleton(dep)
            else:
                return self.__get_transient(dep)

        return None

    def __get_singleton(self, dependency: DependencyConfig):
        if self.__singleton.get(dependency.base.__name__) is None:
            self.__singleton[dependency.base.__name__] = dependency.implement()

        return self.__singleton[dependency.base.__name__]

    def __get_scoped(self, dependency: DependencyConfig):
        sessionid = self.__get_session_id()
        if self.__scoped.get(sessionid).get(dependency.base.__name__) is None:
            self.__scoped.get(sessionid)[dependency.base.__name__] = dependency.implement()

        return self.__scoped.get(sessionid)[dependency.base.__name__]

    def __get_transient(self, dependency: DependencyConfig):
        return dependency.implement()
