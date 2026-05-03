from dataclasses import dataclass

@dataclass
class SubmitCredentialsCommand:
    email: str
    password: str