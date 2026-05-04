from dataclasses import dataclass

from core.application.base_usecase import IUseCase
from core.domain.result import Result

@dataclass
class UpdateNotificationCommand:
    pass

@dataclass
class UpdateNotificationResult:
    pass


class UpdateNotificationUsecase(IUseCase[UpdateNotificationResult, UpdateNotificationCommand]):
    async def call_async(self, params) -> Result[UpdateNotificationResult]:
        return await super().call_async(params)