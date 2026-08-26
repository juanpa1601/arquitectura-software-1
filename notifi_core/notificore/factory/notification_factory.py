"""Fábrica de senders/reglas de notificación.

Implementa el patrón Factory: lee la tabla RULE_CONFIGURATION para construir
el Adapter correcto, envolverlo en NotificationDecorator y ensamblar una
GenericNotificationRule. El mapeo canal -> adapter es una búsqueda en
diccionario (no un if/elif encadenado), así que registrar un canal nuevo es
un cambio de datos aquí, no un cambio en el código de reglas o servicio.
"""
from typing import Type

from notificore.delivery.email_adapter import EmailAdapter
from notificore.delivery.notification_decorator import NotificationDecorator
from notificore.delivery.notification_sender import NotificationSender
from notificore.delivery.push_adapter import PushAdapter
from notificore.delivery.sms_adapter import SmsAdapter
from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.factory.rule_configuration import RULE_CONFIGURATION
from notificore.rules.generic_notification_rule import GenericNotificationRule
from notificore.rules.notification_rule import NotificationRule

_CHANNEL_BUILDERS: dict[str, Type[NotificationSender]] = {
    "sms": SmsAdapter,
    "email": EmailAdapter,
    "push": PushAdapter,
}

class NotificationFactory:
    def create_rule(
        self, 
        event: Event, 
        recipient: Recipient
    ) -> NotificationRule:
        config: dict = RULE_CONFIGURATION.get(
            (
                event.type, 
                recipient.role
            )
        )
        if config is None:
            raise ValueError(
                f"No hay configuración de notificación para el evento "
                f"'{event.type}' y el rol de destinatario '{recipient.role}'"
            )

        builder: Type[NotificationSender] = _CHANNEL_BUILDERS.get(config["channel"])
        if builder is None:
            raise ValueError(f"No hay adaptador registrado para el canal '{config['channel']}'")

        base_sender: NotificationSender = builder()
        decorated_sender: NotificationSender = NotificationDecorator(
            base_sender, 
            config["max_retries"]
        )
        return GenericNotificationRule(decorated_sender)
