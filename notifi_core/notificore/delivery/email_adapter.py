"""Adapter del canal de email.

Implementa el patrón Adapter: adapta la interfaz NotificationSender a una
llamada (simulada) al SDK externo de email.
"""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient

class EmailAdapter(NotificationSender):
    def send(
        self, 
        recipient: Recipient, 
        message: str
    ) -> None:
        print(f"[Email SDK] Enviando correo a {recipient.email}: {message}")
