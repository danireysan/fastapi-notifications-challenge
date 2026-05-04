from abc import ABC, abstractmethod

from core.auth.domain.entities.user_entity import UserEntity
from core.domain.failure import Failure
from core.domain.result import Result



class TokenRepository(ABC):
    @abstractmethod
    async def generate(self, user: UserEntity) -> Result[str]:
        pass