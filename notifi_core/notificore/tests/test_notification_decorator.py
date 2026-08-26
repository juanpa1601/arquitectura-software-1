"""Tests para notificore.delivery.notification_decorator."""
import pytest

from notificore.delivery.notification_decorator import NotificationDecorator
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient


class _FailThenSucceedSender(NotificationSender):
    def __init__(self, fail_times: int) -> None:
        self.fail_times = fail_times
        self.calls = 0

    def send(self, recipient: Recipient, message: str) -> None:
        self.calls += 1
        if self.calls <= self.fail_times:
            raise ConnectionError("canal caído")


class _AlwaysFailingSender(NotificationSender):
    def __init__(self) -> None:
        self.calls = 0

    def send(self, recipient: Recipient, message: str) -> None:
        self.calls += 1
        raise ConnectionError("canal caído")


RECIPIENT = Recipient(role="customer", phone="+1", device_id=1, email="a@b.com")


def test_decorator_retries_until_success():
    inner = _FailThenSucceedSender(fail_times=2)
    decorator = NotificationDecorator(inner, max_retries=3)

    decorator.send(RECIPIENT, "hola")

    assert inner.calls == 3


def test_decorator_raises_after_exhausting_retries():
    inner = _AlwaysFailingSender()
    decorator = NotificationDecorator(inner, max_retries=3)

    with pytest.raises(RuntimeError):
        decorator.send(RECIPIENT, "hola")

    assert inner.calls == 3
