"""Tests para notificore.entities.recipient."""
from notificore.entities.recipient import Recipient


def test_recipient_stores_all_fields():
    recipient = Recipient(role="customer", phone="+1234567890", device_id=42, email="a@b.com")

    assert recipient.role == "customer"
    assert recipient.phone == "+1234567890"
    assert recipient.device_id == 42
    assert recipient.email == "a@b.com"
