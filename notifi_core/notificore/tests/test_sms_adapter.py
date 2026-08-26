"""Tests para notificore.delivery.sms_adapter."""
from notificore.delivery.notification_sender import NotificationSender
from notificore.delivery.sms_adapter import SmsAdapter
from notificore.entities.recipient import Recipient


def test_sms_adapter_is_a_notification_sender():
    assert isinstance(SmsAdapter(), NotificationSender)


def test_sms_adapter_send_does_not_raise(capsys):
    recipient = Recipient(role="customer", phone="+1234567890", device_id=1, email="a@b.com")

    SmsAdapter().send(recipient, "hola")

    captured = capsys.readouterr()
    assert "+1234567890" in captured.out
