from dataclasses import dataclass

from core.application.base_usecase import IUseCase
from core.domain.result import Result


@dataclass
class CreateNotificationCommand:
    pass

@dataclass
class CreateNotificatinoResult:
    pass

class CreateNotificationUsecase(IUseCase[CreateNotificationCommand, CreateNotificatinoResult]):
    async def call_async(self, params) -> Result[CreateNotificatinoResult]:
        return await super().call_async(params)