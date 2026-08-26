"""
Reglas de descuento concretas y su contrato base.

Se reexportan aquí para que consumidores como `factory.py` puedan hacer
`from rules import DiscountRule, VipCustomerRule, ...` sin importar cada
archivo por separado (evita imports redundantes por cada regla nueva).
"""

from .base import DiscountRule
from .corporate_customer_rule import CorporateCustomerRule
from .frequent_customer_rule import FrequentCustomerRule
from .new_customer_books_rule import NewCustomerBooksRule
from .new_customer_general_rule import NewCustomerGeneralRule
from .vip_customer_rule import VipCustomerRule

__all__ = [
    "DiscountRule",
    "NewCustomerBooksRule",
    "NewCustomerGeneralRule",
    "FrequentCustomerRule",
    "VipCustomerRule",
    "CorporateCustomerRule",
]
