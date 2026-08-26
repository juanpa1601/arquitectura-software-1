"""Servicio de notificaciones.

Actúa como raíz de composición del pipeline de notificaciones (patrón
Composition): mantiene una NotificationFactory y le pide una
NotificationRule en el momento de notificar, de modo que la combinación
concreta de canal/decorador/regla se resuelve en cada evento y no queda
fija en la construcción del servicio.
"""
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.factory.notification_factory import NotificationFactory
from notificore.rules.notification_rule import NotificationRule

class NotificationService:
    def __init__(
        self, 
        factory: NotificationFactory
    ) -> None:
        self._factory = factory

    def notify(
        self, 
        event: Event, 
        recipient: Recipient, 
        message: str
    ) -> None:
        rule: NotificationRule = self._factory.create_rule(
            event, 
            recipient
        )
        rule.resolve(
            event, 
            recipient, 
            message
        )
