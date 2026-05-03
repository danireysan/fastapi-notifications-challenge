from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    async def add_user():
        pass

    @abstractmethod
    async def is_user_unique():
        pass