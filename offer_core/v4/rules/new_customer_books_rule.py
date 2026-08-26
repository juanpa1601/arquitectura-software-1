"""Regla: clientes nuevos no reciben descuento en libros."""

from __future__ import annotations

from typing import ClassVar

from domain import (
    Customer, 
    Order
)

from .base import DiscountRule

class NewCustomerBooksRule(DiscountRule):
    """Caso especial: clientes NUEVOS no reciben descuento en LIBROS."""

    priority: ClassVar[int] = 2

    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        return customer.customer_type == "NUEVO" and order.category == "LIBROS"

    def calculate(
        self, 
        order: Order
    ) -> float:
        return 0.0
