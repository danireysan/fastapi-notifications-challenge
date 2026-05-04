

from core.application.base_usecase import IUseCase
from core.auth.application.submit_credentials_command import SubmitCredentialsCommand
from core.auth.application.submit_credentials_result import SubmitCredentialsResult


class LoginUseCase(IUseCase[SubmitCredentialsResult, SubmitCredentialsCommand]):
    async def call_async(self, params):
        return await super().call_async(params)