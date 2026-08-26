"""Decorador de reintentos/logging para notification senders.

Implementa el patrón Decorator: envuelve cualquier NotificationSender con
lógica de reintentos y logging de trazabilidad por cada intento, sin que
el sender envuelto ni sus llamadores necesiten saberlo.
"""
import logging

from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient

logger: logging.Logger = logging.getLogger(__name__)

class NotificationDecorator(NotificationSender):
    def __init__(
        self, 
        sender: NotificationSender, 
        max_retries: int
    ) -> None:
        self._sender = sender
        self._max_retries = max_retries

    def send(
        self, 
        recipient: Recipient, 
        message: str
    ) -> None:
        last_error: Exception | None = None
        for attempt in range(1, self._max_retries + 1):
            try:
                logger.info(
                    "Intento %d/%d usando %s",
                    attempt,
                    self._max_retries,
                    type(self._sender).__name__,
                )
                self._sender.send(
                    recipient, 
                    message
                )
                logger.info("Intento %d exitoso", attempt)
                return
            except Exception as error:  # noqa: BLE001 - frontera de reintentos, es intencional
                last_error = error
                logger.warning("Intento %d fallido: %s", attempt, error)

        logger.error("Los %d intentos fallaron", self._max_retries)
        raise RuntimeError(
            f"No se pudo enviar la notificación tras {self._max_retries} intentos"
        ) from last_error
