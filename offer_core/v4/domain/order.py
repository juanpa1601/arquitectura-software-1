"""Entidad de dominio: pedido."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Order:
    """
    Representa el pedido sobre el cual se calcula el descuento.

    `category` se mantiene como `str` por la misma razón que `Customer.customer_type`:
    debe poder extenderse sin tocar código existente.
    Valores usados actualmente: "ELECTRONICA", "HOGAR", "LIBROS", ...
    """

    category: str
    subtotal: float
