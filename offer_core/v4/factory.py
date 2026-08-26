"""Composición del servicio (ej. en el arranque de la app / inyección de dependencias)."""

from __future__ import annotations

from rules import (
    CorporateCustomerRule,
    FrequentCustomerRule,
    NewCustomerBooksRule,
    NewCustomerGeneralRule,
    VipCustomerRule,
)
from services import DiscountService

def build_discount_service() -> DiscountService:
    """Construye el servicio de descuentos con todas las reglas de negocio registradas."""
    service: DiscountService = DiscountService()
    service.add_rule(NewCustomerBooksRule())
    service.add_rule(NewCustomerGeneralRule())
    service.add_rule(FrequentCustomerRule())
    service.add_rule(VipCustomerRule())
    service.add_rule(CorporateCustomerRule())
    return service
