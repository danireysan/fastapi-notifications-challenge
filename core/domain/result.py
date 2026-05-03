from __future__ import annotations
from typing import Awaitable, Generic, TypeVar, Callable, Any


from core.domain.failure import Failure

# T is for a value you return
T = TypeVar("T")
# U is what you get after a transformation
U = TypeVar("U")


class Result(Generic[T]):
    def __init__(self, value: T | Failure):
        self._value = value
        super().__init__()

    @property
    def is_success(self) -> bool:
        return not isinstance(self._value, Failure)

    def unwrap(self) -> T:
        if isinstance(self._value, Failure):
            raise ValueError("Cannot unwrap a Failure")
        return self._value

    def failure(self) -> Failure:
        return self._value

    def map(self, func: Callable[[T], U]) -> Result[U]:
        if not self.is_success:
            return Result(self._value)
        return Result(func(self.unwrap()))

    def bind(self, func: Callable[[T], Result[U]]):
        if not self.is_success:
            return Result(self._value)
        return func(self.unwrap())
    
    async def async_bind(self, func: Callable[[T], Awaitable[Result[U]]]) -> Result[U]:
        if not self.is_success:
            return self
        return await func(self.unwrap())

    @staticmethod
    def success(val: T) -> Result[T]:
        return Result(val)

    @staticmethod
    def fail(msg: str) -> Result[Any]:
        return Result(Failure(msg))
