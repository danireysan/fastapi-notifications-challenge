from dataclasses import dataclass

from pwdlib import PasswordHash

from core.auth.domain.value_objects.email_address import EmailAddress
from core.auth.domain.value_objects.user_id import UserId


@dataclass
class UserEntity:
    id: UserId
    email: EmailAddress
    password_hash: PasswordHash

    @staticmethod
    def create(id: UserId, email: EmailAddress, password_hash: PasswordHash) -> "UserEntity":
        return UserEntity(id, email, password_hash)