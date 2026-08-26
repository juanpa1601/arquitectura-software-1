"""Regla para clientes corporativos."""

from __future__ import annotations

from typing import ClassVar

from domain import (
    Customer, 
    Order
)

from .base import DiscountRule

class CorporateCustomerRule(DiscountRule):
    """
    Nuevo tipo de cliente anunciado por producto.
    NOTA: esta es la ÚNICA clase nueva necesaria para soportar CORPORATIVO.
    No se modificó DiscountService ni ninguna regla existente (cumple OCP).
    """

    priority: ClassVar[int] = 5

    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        return customer.customer_type == "CORPORATIVO"

    def calculate(
        self, 
        order: Order
    ) -> float:
        # Placeholder: ajustar con la regla real que defina el stakeholder.
        return order.subtotal * 0.18
