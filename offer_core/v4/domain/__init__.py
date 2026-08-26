"""
Entidades de dominio del motor de descuentos.

Se reexportan aquí para que el resto del código pueda hacer
`from domain import Customer, Order` sin conocer en qué archivo
vive cada clase, evitando imports redundantes o rutas frágiles.
"""

from .customer import Customer
from .order import Order

__all__ = ["Customer", "Order"]
