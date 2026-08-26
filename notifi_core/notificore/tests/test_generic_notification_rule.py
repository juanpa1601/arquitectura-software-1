"""Tests para notificore.rules.generic_notification_rule."""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.rules.generic_notification_rule import GenericNotificationRule


class _SpySender(NotificationSender):
    def __init__(self) -> None:
        self.received = None

    def send(self, recipient: Recipient, message: str) -> None:
        self.received = (recipient, message)


def test_resolve_delegates_to_injected_sender():
    spy = _SpySender()
    rule = GenericNotificationRule(spy)
    event = Event(type="order_created")
    recipient = Recipient(role="customer", phone="+1", device_id=1, email="a@b.com")

    rule.resolve(event, recipient, "hola")

    assert spy.received == (recipient, "hola")
