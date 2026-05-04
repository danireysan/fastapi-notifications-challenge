from dataclasses import dataclass

from core.application.base_usecase import IUseCase

@dataclass
class DeleteNotificationCommand:
    pass

@dataclass
class DeleteNotificationResult:
    pass


class DeleteNotificationUseCase(IUseCase[DeleteNotificationResult, DeleteNotificationCommand]):
    async def call_async(self, params):
        return await super().call_async(params)