from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class SendResult:
    sendAt: datetime
    metadata: Optional[str]