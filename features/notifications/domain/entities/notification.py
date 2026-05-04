from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from features.notifications.domain.entities.notification_channel import NotificationChannel
from features.notifications.domain.entities.notification_id import NotificationId


@dataclass
class Notification:
    id: NotificationId
    title: str
    content: str
    recipient: str
    created_by: str
    channel: NotificationChannel
    sent_at: Optional[datetime]
    send_metadata: Optional[str]

    @staticmethod
    def create(
        title: str,
        content: str,
        recipient: str,
        created_by: str,
        channel: NotificationChannel,
        sent_at: Optional[datetime] = None,
        send_metadata: Optional[str] = None,
    ) -> "Notification":
        return Notification(
            id=NotificationId.new(),
            title=title,
            content=content,
            recipient=recipient,
            created_by=created_by,
            channel=channel,
            sent_at=sent_at,
            send_metadata=send_metadata,
        )
