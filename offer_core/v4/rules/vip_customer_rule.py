"""Regla para clientes VIP."""

from __future__ import annotations

from typing import ClassVar

from domain import (
    Customer, 
    Order
)

from .base import DiscountRule

class VipCustomerRule(DiscountRule):
    """Regla para clientes VIP: tasa fija sin importar la categoría."""

    priority: ClassVar[int] = 4

    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        return customer.customer_type == "VIP"

    def calculate(
        self, 
        order: Order
    ) -> float:
        return order.subtotal * 0.20
