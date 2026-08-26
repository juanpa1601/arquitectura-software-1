"""Regla para clientes frecuentes."""

from __future__ import annotations

from typing import ClassVar

from domain import (
    Customer, 
    Order
)

from .base import DiscountRule

class FrequentCustomerRule(DiscountRule):
    """Regla para clientes FRECUENTES, varía por categoría."""

    priority: ClassVar[int] = 3

    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        return customer.customer_type == "FRECUENTE"

    def calculate(
        self, 
        order: Order
    ) -> float:
        rates: dict[str, float] = {"ELECTRONICA": 0.08, "HOGAR": 0.15}
        return order.subtotal * rates.get(order.category, 0.12)
