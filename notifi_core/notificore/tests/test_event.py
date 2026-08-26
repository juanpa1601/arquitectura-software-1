"""Tests para notificore.entities.event."""
from notificore.entities.event import Event


def test_event_stores_type():
    event = Event(type="order_created")

    assert event.type == "order_created"
