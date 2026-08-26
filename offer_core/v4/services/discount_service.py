"""Orquestador de reglas de descuento."""

from __future__ import annotations

from domain import (
    Customer, 
    Order
)
from rules import DiscountRule

class DiscountService:
    """
    Orquesta la evaluación de reglas de descuento.
    No conoce ninguna regla concreta: solo sabe que recibe objetos
    que cumplen el contrato DiscountRule.
    """

    def __init__(self) -> None:
        self._rules: list[DiscountRule] = []

    def add_rule(
        self, 
        rule: DiscountRule
    ) -> None:
        self._rules.append(rule)

    def calculate_discount(
        self, 
        order: Order, 
        customer: Customer
    ) -> float:
        # 1. Ordenar por prioridad descendente: la más específica primero.
        sorted_rules: list[DiscountRule] = sorted(
            self._rules, 
            key=lambda rule: rule.priority, 
            reverse=False
        )

        # 2. Recorrer y detenerse en la primera regla que aplique.
        for rule in sorted_rules:
            if rule.applies(customer, order):
                return rule.calculate(order)

        # 3. Caso por defecto: ninguna regla aplicó.
        return 0.0
