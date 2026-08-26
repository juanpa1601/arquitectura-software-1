"""Adapter del canal de notificaciones push.

Implementa el patrón Adapter: adapta la interfaz NotificationSender a una
llamada (simulada) al SDK externo de notificaciones push.
"""
from notificore.delivery.notification_sender import NotificationSender
from notificore.entities.recipient import Recipient

class PushAdapter(NotificationSender):
    def send(
        self, 
        recipient: Recipient, 
        message: str
    ) -> None:
        print(f"[Push SDK] Enviando push al dispositivo {recipient.device_id}: {message}")
