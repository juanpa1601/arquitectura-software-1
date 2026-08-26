"""Tests para notificore.delivery.push_adapter."""
from notificore.delivery.notification_sender import NotificationSender
from notificore.delivery.push_adapter import PushAdapter
from notificore.entities.recipient import Recipient


def test_push_adapter_is_a_notification_sender():
    assert isinstance(PushAdapter(), NotificationSender)


def test_push_adapter_send_does_not_raise(capsys):
    recipient = Recipient(role="customer", phone="+1", device_id=99, email="a@b.com")

    PushAdapter().send(recipient, "hola")

    captured = capsys.readouterr()
    assert "99" in captured.out
