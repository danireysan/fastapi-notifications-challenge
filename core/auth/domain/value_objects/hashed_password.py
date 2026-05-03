from dataclasses import dataclass
from typing import Optional

from core.domain.result import Result


@dataclass(frozen=True)
class HashedPassword:
    value: str

    @staticmethod
    def from_persistence(value: str) -> "HashedPassword":
        return HashedPassword(value=value)

    @staticmethod
    def from_persistance(value: str) -> "HashedPassword":
        return HashedPassword.from_persistence(value=value)

    @staticmethod
    def create(value: Optional[str]) -> Result["HashedPassword"]:
        if not value or not value.strip():
            return Result.fail("Password is required")

        return Result.success(HashedPassword(value=value))

    def __str__(self) -> str:
        return self.value
