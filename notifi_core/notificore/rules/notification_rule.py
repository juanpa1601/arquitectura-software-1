"""Interfaz NotificationRule.

Define la interfaz Strategy que desacopla "qué debe pasar para un
evento/destinatario/mensaje dado" de cómo se entrega realmente el mensaje,
lo cual queda a cargo del NotificationSender que se inyecte.
"""
from abc import (
    ABC, 
    abstractmethod
)

from notificore.entities.event import Event
from notificore.entities.recipient import Recipient

class NotificationRule(ABC):
    @abstractmethod
    def resolve(
        self, 
        event: Event, 
        recipient: Recipient, 
        message: str
    ) -> None:
        raise NotImplementedError
