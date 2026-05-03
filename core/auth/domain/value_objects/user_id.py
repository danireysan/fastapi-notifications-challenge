from dataclasses import dataclass
import uuid

@dataclass(frozen=True)
class UserId:
    value: str
    
    @staticmethod
    def new() -> "UserId":
        return UserId(str(uuid.uuid4()))
    
    def __str__(self):
        return self.value


