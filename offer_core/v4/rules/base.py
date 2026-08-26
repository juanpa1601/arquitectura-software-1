"""Abstracción: contrato que toda regla de descuento debe cumplir."""

from __future__ import annotations

from abc import (
    ABC, 
    abstractmethod
)
from typing import ClassVar

from domain import (
    Customer, 
    Order
)

class DiscountRule(ABC):
    """
    Contrato para una regla de descuento.

    `priority`: entre mayor el valor, más específica/precedente es la regla.
    Se usa para desempatar cuando varias reglas podrían aplicar al mismo
    (customer, order) -- p.ej. "NUEVO + LIBROS" (prioridad alta) debe ganarle
    a "NUEVO" en general (prioridad baja).
    """

    priority: ClassVar[int] = 0

    @abstractmethod
    def applies(
        self, 
        customer: Customer, 
        order: Order
    ) -> bool:
        """Indica si esta regla es válida para este cliente y pedido."""
        raise NotImplementedError

    @abstractmethod
    def calculate(
        self, 
        order: Order
    ) -> float:
        """Calcula el monto del descuento, asumiendo que `applies` ya dio True."""
        raise NotImplementedError
