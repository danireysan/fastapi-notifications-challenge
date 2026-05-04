import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class NotificationId:
    value: str

    @staticmethod
    def new() -> "NotificationId":
        return NotificationId(value=str(uuid.uuid4()))

    @staticmethod
    def from_string(value: str) -> "NotificationId":
        return NotificationId(value=value)

    def __str__(self) -> str:
        return self.value
