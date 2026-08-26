"""Interfaz NotificationSender.

Define la interfaz Target común del patrón Adapter: cada canal concreto
(SMS, email, push) y el Decorator de reintentos implementan este mismo
contrato, así los llamadores nunca dependen del SDK de un canal específico.
"""
from abc import (
    ABC, 
    abstractmethod
)

from notificore.entities.recipient import Recipient

class NotificationSender(ABC):
    @abstractmethod
    def send(
        self, 
        recipient: Recipient, 
        message: str
    ) -> None:
        raise NotImplementedError
