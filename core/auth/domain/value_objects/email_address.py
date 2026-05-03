import re
from dataclasses import dataclass
from typing import Optional

from core.domain.result import Result

EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"
)


@dataclass(frozen=True)
class EmailAddress:
    value: str

    @staticmethod
    def from_persistance(value: str) -> "EmailAddress":
        return EmailAddress(value=value)

    @staticmethod
    def from_persistence(value: str) -> "EmailAddress":
        return EmailAddress.from_persistance(value=value)

    @staticmethod
    def create(value: Optional[str]) -> Result["EmailAddress"]:
        if value is None:
            return Result.fail("Email is required")

        normalized = value.strip().lower()
        if not normalized:
            return Result.fail("Email is required")

        if len(normalized) > 254:
            return Result.fail("Email is too long")

        local_part, _, domain_part = normalized.partition("@")
        if not local_part or not domain_part:
            return Result.fail("Email format is invalid")

        if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
            return Result.fail("Email format is invalid")

        if domain_part.startswith("-") or domain_part.endswith("-") or ".." in domain_part:
            return Result.fail("Email format is invalid")

        if not EMAIL_REGEX.fullmatch(normalized):
            return Result.fail("Email format is invalid")

        return Result.success(EmailAddress(value=normalized))

    def __str__(self) -> str:
        return self.value