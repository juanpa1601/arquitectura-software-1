"""Tests para notificore.service.notification_service.

También verifica la propiedad clave de extensibilidad del sistema: agregar
un canal/proveedor de entrega totalmente nuevo (simulado aquí con un
adapter falso inyectado a través de una fábrica falsa) no requiere cambios
en GenericNotificationRule ni en NotificationService — ambos solo dependen
de las interfaces NotificationSender y NotificationRule.
"""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.rules.generic_notification_rule import GenericNotificationRule
from notificore.rules.notification_rule import NotificationRule
from notificore.service.notification_service import NotificationService


class _FakeNewChannelAdapter(NotificationSender):
    """Representa un canal/proveedor nuevo que antes no existía."""

    def __init__(self) -> None:
        self.sent_to = None

    def send(self, recipient: Recipient, message: str) -> None:
        self.sent_to = (recipient, message)


class _FakeFactory:
    def __init__(self, rule: NotificationRule) -> None:
        self._rule = rule

    def create_rule(self, event: Event, recipient: Recipient) -> NotificationRule:
        return self._rule


def test_notify_delegates_to_factory_and_rule():
    fake_adapter = _FakeNewChannelAdapter()
    rule = GenericNotificationRule(fake_adapter)
    service = NotificationService(_FakeFactory(rule))
    event = Event(type="order_created")
    recipient = Recipient(role="customer", phone="+1", device_id=1, email="a@b.com")

    service.notify(event, recipient, "hola")

    assert fake_adapter.sent_to == (recipient, "hola")


def test_new_channel_requires_no_changes_to_rule_or_service():
    """Un NotificationSender totalmente nuevo se conecta sin tocar el
    código fuente de GenericNotificationRule ni de NotificationService."""
    fake_adapter = _FakeNewChannelAdapter()

    rule = GenericNotificationRule(fake_adapter)
    service = NotificationService(_FakeFactory(rule))

    event = Event(type="new_event_type")
    recipient = Recipient(role="new_role", phone="+1", device_id=1, email="a@b.com")
    service.notify(event, recipient, "mensaje nuevo canal")

    assert fake_adapter.sent_to == (recipient, "mensaje nuevo canal")
