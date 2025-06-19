from abc import ABC, abstractmethod
from typing import Any


class UserRepository(ABC):
    def __init__(self, username: str) -> None:
        self.__username = username

    @property
    @abstractmethod
    def username(self):
        pass

    @abstractmethod
    def save_user(self, user_data):
        pass

    @classmethod
    @abstractmethod
    def save_cls(cls, user_data):
        pass


class InMemoryUserRepository(UserRepository):
    def __init__(self, username: str) -> None:
        self.__username = username

    def username(self):
        self.__username

    def save_user(self, user_data):
        print(f"User {self} saved.")

    @classmethod
    def save_cls(cls, user_data):
        print(f"User {cls} saved.")


user_repository = InMemoryUserRepository(username="Yiiiisus")
user_repository.save_cls([])


class DunderMethods:
    def __call__(self, data) -> Any:
        print("Now in __call__ method")
        self.data = data


call_object = DunderMethods()
call_object(data=2)


class LengthValidator:
    def __init__(self, min_len=0, max_len=None):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, value):
        if not isinstance(value, str):
            raise TypeError("Only strings are supported")

        if len(value) < self.min_len:
            raise ValueError(f"String is too short (min {self.min_len})")

        if self.max_len is not None and len(value) > self.max_len:
            raise ValueError(f"String is too long (max {self.max_len})")

        return True

    def __repr__(self) -> str:
        return "JIIJJIJI qué divertido verdad?"


username_validator = LengthValidator(2, 6)
print(username_validator)
# print(username_validator("J")) # Raises ValueError
print(username_validator("Ju"))  # True
print(username_validator("Jua"))  # True
print(username_validator("Juan"))  # True
