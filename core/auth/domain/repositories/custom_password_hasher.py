from abc import ABC, abstractmethod

from core.auth.domain.value_objects.hashed_password import HashedPassword
from core.auth.domain.value_objects.user_id import UserId
from core.domain.failure import Failure
from core.domain.result import Result


class CustomPasswordHasher(ABC):
    @abstractmethod
    async def hash_password(id: UserId, password: str) -> Result[Failure, HashedPassword]:
        pass

    @abstractmethod
    async def verify_password(id: UserId, password: str) -> Result[Failure, bool]:
        pass