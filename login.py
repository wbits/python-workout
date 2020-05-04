import unittest


class User:
    def __init__(self, name: str, secret: str):
        self.name = name
        self.secret = secret


class UserRepository:
    __users = {}

    def __init__(self, *users: User):
        for user in users:
            self.save(user)

    def save(self, user: User):
        self.__users.update({user.name: user})

    def find(self, name: str) -> User:
        if name not in self.__users.keys():
            raise Exception

        return self.__users.get(name)


class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def login(self, name: str, secret: str) -> bool:
        try:
            user = self.__repository.find(name)
        except Exception:
            return False

        return user.secret is secret


class LoginTestCase(unittest.TestCase):
    def test_login_with_username_and_password(self):
        repository = UserRepository(User('dick', 'secret'), User('foo', 'bar'))
        user_service = UserService(repository)

        self.assertTrue(user_service.login('dick', 'secret'))
        self.assertTrue(user_service.login('foo', 'bar'))
