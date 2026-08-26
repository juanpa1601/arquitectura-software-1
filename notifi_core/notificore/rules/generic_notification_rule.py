"""Regla de notificación genérica.

Implementa la estrategia concreta del patrón Strategy: cumple
NotificationRule delegando en un NotificationSender inyectado, por lo que
nunca necesita saber qué canal o decorador hay detrás de esa interfaz.
"""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.rules.notification_rule import NotificationRule


class GenericNotificationRule(NotificationRule):
    def __init__(
        self, 
        sender: NotificationSender
    ) -> None:
        self._sender = sender

    def resolve(
        self, 
        event: Event, 
        recipient: Recipient, 
        message: str
    ) -> None:
        self._sender.send(
            recipient, 
            message
        )
