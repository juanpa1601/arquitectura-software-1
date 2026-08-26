"""
OfferCore - Motor de descuentos del checkout
----------------------------------------------
Refactorización aplicando SRP y OCP:
- DiscountService ya NO conoce reglas concretas, solo la abstracción DiscountRule.
- Agregar un nuevo tipo de cliente o categoría = agregar una nueva clase,
  sin modificar código existente (DiscountService, DiscountRule, ni las demás reglas).

El código está organizado en subpaquetes por responsabilidad:
- domain/    -> entidades del dominio (Customer, Order)
- rules/     -> contrato DiscountRule y sus implementaciones concretas
- services/  -> orquestador DiscountService
- factory.py -> composición / inyección de dependencias del servicio
"""

from __future__ import annotations

from domain import (
    Customer, 
    Order
)
from factory import build_discount_service

from services import DiscountService

if __name__ == "__main__":
    service: DiscountService = build_discount_service()

    # Casos de verificación manual (equivalentes a los del diseño original).
    cases: list[tuple[Customer, Order]] = [
        (Customer("NUEVO"), Order("ELECTRONICA", 100_000)),
        (Customer("NUEVO"), Order("LIBROS", 100_000)),  # caso especial
        (Customer("FRECUENTE"), Order("HOGAR", 100_000)),
        (Customer("VIP"), Order("ELECTRONICA", 100_000)),
        (Customer("CORPORATIVO"), Order("HOGAR", 100_000)),  # nuevo tipo
    ]

    for customer, order in cases:
        discount: float = service.calculate_discount(
            order, 
            customer
        )
        print(f"{customer.customer_type:12} + {order.category:12} -> descuento: {discount:.2f}")
