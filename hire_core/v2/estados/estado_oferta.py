from __future__ import annotations

from .estado_base import EstadoBase


class EstadoOferta(EstadoBase):
    def nombre_estado(self) -> str:
        return "OFERTA"

    def transicion(self) -> str | None:
        return "VERIFICACION_REFERENCIAS"
