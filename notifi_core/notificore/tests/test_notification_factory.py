"""Tests para notificore.factory.notification_factory."""
import pytest

from notificore.delivery.email_adapter import EmailAdapter
from notificore.delivery.notification_decorator import NotificationDecorator
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.factory.notification_factory import NotificationFactory
from notificore.rules.generic_notification_rule import GenericNotificationRule
from notificore.rules.notification_rule import NotificationRule


def test_create_rule_builds_configured_channel():
    factory = NotificationFactory()
    event = Event(type="order_created")
    recipient = Recipient(role="customer", phone="+1", device_id=1, email="a@b.com")

    rule = factory.create_rule(event, recipient)

    assert isinstance(rule, NotificationRule)
    assert isinstance(rule, GenericNotificationRule)
    assert isinstance(rule._sender, NotificationDecorator)
    assert isinstance(rule._sender._sender, EmailAdapter)
    assert rule._sender._max_retries == 3


def test_create_rule_raises_for_unknown_combination():
    factory = NotificationFactory()
    event = Event(type="unknown_event")
    recipient = Recipient(role="ghost", phone="+1", device_id=1, email="a@b.com")

    with pytest.raises(ValueError):
        factory.create_rule(event, recipient)
