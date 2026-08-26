"""Adapter del canal SMS.

Implementa el patrón Adapter: adapta la interfaz NotificationSender a una
llamada (simulada) al SDK externo de SMS.
"""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient

class SmsAdapter(NotificationSender):
    def send(
        self, 
        recipient: Recipient, 
        message: str
    ) -> None:
        print(f"[SMS SDK] Enviando SMS a {recipient.phone}: {message}")
