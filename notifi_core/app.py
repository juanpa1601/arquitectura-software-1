"""Script de ejemplo que ejecuta NotifiCore de punta a punta.

No es parte del dominio (no agrega reglas ni canales nuevos): simplemente
arma un NotificationService con su NotificationFactory y dispara notify()
para un par de combinaciones evento/destinatario, para ver el sistema
funcionando en consola.
"""
import logging

from notificore.entities.event import Event
from notificore.entities.recipient import Recipient
from notificore.factory.notification_factory import NotificationFactory
from notificore.service.notification_service import NotificationService

def main() -> None:
    logging.basicConfig(
        level=logging.INFO, 
        format="%(levelname)s %(name)s: %(message)s"
    )

    service: NotificationService = NotificationService(NotificationFactory())

    cliente: Recipient = Recipient(
        role="customer", 
        phone="+34600111222", 
        device_id=101, 
        email="cliente@example.com"
    )
    admin: Recipient = Recipient(
        role="admin", 
        phone="+34600333444", 
        device_id=202, 
        email="admin@example.com"
    )

    print("\n--- order_created -> customer (canal: email) ---")
    service.notify(
        Event(type="order_created"), 
        cliente, 
        "Tu pedido fue creado con éxito."
    )

    print("\n--- order_created -> admin (canal: push) ---")
    service.notify(
        Event(type="order_created"), 
        admin, 
        "Se creó un nuevo pedido."
    )

    print("\n--- payment_failed -> customer (canal: sms) ---")
    service.notify(
        Event(type="payment_failed"), 
        cliente, 
        "Tu pago no pudo procesarse."
    )

    print("\n--- combinación no configurada ---")
    try:
        service.notify(
            Event(type="account_deleted"), 
            cliente, 
            "Tu cuenta fue eliminada."
        )
    except ValueError as error:
        print(f"Error esperado: {error}")


if __name__ == "__main__":
    main()
