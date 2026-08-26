"""Tests para notificore.delivery.email_adapter."""
from notificore.delivery.email_adapter import EmailAdapter
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient


def test_email_adapter_is_a_notification_sender():
    assert isinstance(EmailAdapter(), NotificationSender)


def test_email_adapter_send_does_not_raise(capsys):
    recipient = Recipient(role="customer", phone="+1", device_id=1, email="a@b.com")

    EmailAdapter().send(recipient, "hola")

    captured = capsys.readouterr()
    assert "a@b.com" in captured.out
