"""
OfferCore - Motor de descuentos del checkout
----------------------------------------------
Refactorización aplicando SRP y OCP:
- DescuentoService ya NO conoce reglas concretas, solo la abstracción DiscountRule.
- Agregar un nuevo tipo de cliente o categoría = agregar una nueva clase,
  sin modificar código existente (DescuentoService, DiscountRule, ni las demás reglas).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Entidades del dominio
# ---------------------------------------------------------------------------

@dataclass
class Cliente:
    tipo: str  # "NUEVO", "FRECUENTE", "VIP", "CORPORATIVO", ...


@dataclass
class Pedido:
    categoria: str  # "ELECTRONICA", "HOGAR", "LIBROS", ...
    subtotal: float


# ---------------------------------------------------------------------------
# Abstracción: contrato que toda regla de descuento debe cumplir
# ---------------------------------------------------------------------------

class DiscountRule(ABC):
    """
    Contrato para una regla de descuento.

    `prioridad`: entre mayor el valor, más específica/precedente es la regla.
    Se usa para desempatar cuando varias reglas podrían aplicar al mismo
    (cliente, pedido) -- p.ej. "NUEVO + LIBROS" (prioridad alta) debe ganarle
    a "NUEVO" en general (prioridad baja).
    """

    prioridad: int = 0

    @abstractmethod
    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        """Indica si esta regla es válida para este cliente y pedido."""
        raise NotImplementedError

    @abstractmethod
    def calcular(self, pedido: Pedido) -> float:
        """Calcula el monto del descuento, asumiendo que `aplica` ya dio True."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Implementaciones concretas (reglas de negocio actuales)
# ---------------------------------------------------------------------------

class ReglaNuevoLibros(DiscountRule):
    """Caso especial: clientes NUEVOS no reciben descuento en LIBROS."""

    prioridad = 10  # más específica que ReglaNuevoGeneral -> mayor prioridad

    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        return cliente.tipo == "NUEVO" and pedido.categoria == "LIBROS"

    def calcular(self, pedido: Pedido) -> float:
        return 0.0


class ReglaNuevoGeneral(DiscountRule):
    """Regla general para clientes NUEVOS (cualquier categoría, excepto LIBROS)."""

    prioridad = 1

    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        return cliente.tipo == "NUEVO"

    def calcular(self, pedido: Pedido) -> float:
        if pedido.categoria == "ELECTRONICA":
            return pedido.subtotal * 0.05
        return pedido.subtotal * 0.10


class ReglaFrecuente(DiscountRule):
    """Regla para clientes FRECUENTES, varía por categoría."""

    prioridad = 1

    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        return cliente.tipo == "FRECUENTE"

    def calcular(self, pedido: Pedido) -> float:
        tasas = {"ELECTRONICA": 0.08, "HOGAR": 0.15}
        return pedido.subtotal * tasas.get(pedido.categoria, 0.12)


class ReglaVIP(DiscountRule):
    """Regla para clientes VIP: tasa fija sin importar la categoría."""

    prioridad = 1

    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        return cliente.tipo == "VIP"

    def calcular(self, pedido: Pedido) -> float:
        return pedido.subtotal * 0.20


class ReglaCorporativo(DiscountRule):
    """
    Nuevo tipo de cliente anunciado por producto.
    NOTA: esta es la ÚNICA clase nueva necesaria para soportar CORPORATIVO.
    No se modificó DescuentoService ni ninguna regla existente (cumple OCP).
    """

    prioridad = 1

    def aplica(self, cliente: Cliente, pedido: Pedido) -> bool:
        return cliente.tipo == "CORPORATIVO"

    def calcular(self, pedido: Pedido) -> float:
        # Placeholder: ajustar con la regla real que defina el stakeholder.
        return pedido.subtotal * 0.18


# ---------------------------------------------------------------------------
# Orquestador
# ---------------------------------------------------------------------------

class DescuentoService:
    """
    Orquesta la evaluación de reglas de descuento.
    No conoce ninguna regla concreta: solo sabe que recibe objetos
    que cumplen el contrato DiscountRule.
    """

    def __init__(self) -> None:
        self._reglas: list[DiscountRule] = []

    def agregar_regla(self, regla: DiscountRule) -> None:
        self._reglas.append(regla)

    def calcular_descuento(self, pedido: Pedido, cliente: Cliente) -> float:
        # 1. Ordenar por prioridad descendente: la más específica primero.
        reglas_ordenadas = sorted(
            self._reglas, key=lambda r: r.prioridad, reverse=True
        )

        # 2. Recorrer y detenerse en la primera regla que aplique.
        for regla in reglas_ordenadas:
            if regla.aplica(cliente, pedido):
                return regla.calcular(pedido)

        # 3. Caso por defecto: ninguna regla aplicó.
        return 0.0


# ---------------------------------------------------------------------------
# Composición del servicio (ej. en el arranque de la app / inyección de dependencias)
# ---------------------------------------------------------------------------

def construir_servicio_descuentos() -> DescuentoService:
    servicio = DescuentoService()
    servicio.agregar_regla(ReglaNuevoLibros())
    servicio.agregar_regla(ReglaNuevoGeneral())
    servicio.agregar_regla(ReglaFrecuente())
    servicio.agregar_regla(ReglaVIP())
    servicio.agregar_regla(ReglaCorporativo())
    return servicio


# ---------------------------------------------------------------------------
# Ejemplo de uso / verificación manual
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    servicio = construir_servicio_descuentos()

    casos = [
        (Cliente("NUEVO"), Pedido("ELECTRONICA", 100_000)),
        (Cliente("NUEVO"), Pedido("LIBROS", 100_000)),        # caso especial
        (Cliente("FRECUENTE"), Pedido("HOGAR", 100_000)),
        (Cliente("VIP"), Pedido("ELECTRONICA", 100_000)),
        (Cliente("CORPORATIVO"), Pedido("HOGAR", 100_000)),   # nuevo tipo
    ]

    for cliente, pedido in casos:
        descuento = servicio.calcular_descuento(pedido, cliente)
        print(f"{cliente.tipo:12} + {pedido.categoria:12} -> descuento: {descuento:.2f}")