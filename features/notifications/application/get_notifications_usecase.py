from dataclasses import dataclass

from core.application.base_usecase import IUseCase


@dataclass
class GetNotificationResult:
    pass

@dataclass
class GetNotificationCommand:
    pass


class GetNotificationsUsecase(IUseCase[GetNotificationResult, GetNotificationCommand]):
    async def call_async(self, params):
        return await super().call_async(params)