"""Regla general para clientes nuevos."""

from __future__ import annotations

from typing import ClassVar

from domain import (
    Customer, 
    Order
)

from .base import DiscountRule

class NewCustomerGeneralRule(DiscountRule):
    """Regla general para clientes NUEVOS (cualquier categoría, excepto LIBROS)."""

    priority: ClassVar[int] = 1

    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        return customer.customer_type == "NUEVO"

    def calculate(
        self, 
        order: Order
    ) -> float:
        if order.category == "ELECTRONICA":
            return order.subtotal * 0.05
        return order.subtotal * 0.10
