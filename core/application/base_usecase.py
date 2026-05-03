from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from core.domain.failure import Failure
from core.domain.result import Result

T = TypeVar("T", bound=object)
TParams = TypeVar("TParams", contravariant=True)

class IUseCase(ABC, Generic[T, TParams]):
    @abstractmethod
    async def call_async(self, params: TParams ) -> Result:
        pass


