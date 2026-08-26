"""Tabla de configuración estática (event_type, recipient_role) -> canal.

Es el único lugar que decide qué canal y qué política de reintentos aplican
a una combinación de evento/rol dada. Existe para que NotificationFactory
nunca necesite ramificación condicional por tipo de evento o rol: cada
combinación nueva se absorbe como una entrada más del diccionario.
"""
from typing import TypedDict

class RuleConfigEntry(TypedDict):
    channel: str
    max_retries: int

RULE_CONFIGURATION: dict[tuple[str, str], RuleConfigEntry] = {
    ("order_created", "customer"): {"channel": "email", "max_retries": 3},
    ("order_created", "admin"): {"channel": "push", "max_retries": 2},
    ("payment_failed", "customer"): {"channel": "sms", "max_retries": 5},
    ("payment_failed", "admin"): {"channel": "email", "max_retries": 3},
    ("shipment_delayed", "customer"): {"channel": "push", "max_retries": 2},
}
