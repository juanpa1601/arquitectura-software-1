"""Entidad de dominio: cliente."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Customer:
    """
    Representa al cliente que realiza la compra.

    `customer_type` se mantiene como `str` (y no como Enum cerrado) a propósito:
    agregar un nuevo tipo de cliente solo requiere una nueva `DiscountRule`,
    sin modificar esta clase ni ningún enum existente (principio OCP).
    Valores usados actualmente: "NUEVO", "FRECUENTE", "VIP", "CORPORATIVO", ...
    """

    customer_type: str
