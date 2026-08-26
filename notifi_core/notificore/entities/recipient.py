"""Entidad de dominio: Recipient.

Es un value object simple (no involucra ningún patrón de diseño): agrupa
los datos de contacto que el destinatario de un evento puede necesitar en
cualquiera de los canales de entrega.
"""
from dataclasses import dataclass

@dataclass
class Recipient:
    role: str
    phone: str
    device_id: int
    email: str
