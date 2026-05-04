from datetime import datetime, timedelta, timezone

import jwt

from core.auth.domain.entities.user_entity import UserEntity
from core.auth.domain.repositories.token_repository import TokenRepository
from core.domain.failure import Failure
from core.domain.result import Result
from core.settings import settings

_ALGORITHM = "HS256"


class JwtTokenRepository(TokenRepository):
    async def generate(self, user: UserEntity) -> Result[str]:
        try:
            payload = {
                "sub": str(user.id),
                "email": str(user.email),
                "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes),
            }
            token = jwt.encode(payload, settings.secret_key, algorithm=_ALGORITHM)
            return Result(token)
        except Exception as exc:
            return Result(Failure(message=str(exc)))
