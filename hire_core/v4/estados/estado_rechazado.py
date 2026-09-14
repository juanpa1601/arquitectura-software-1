from __future__ import annotations

from .estado_base import EstadoBase


class EstadoRechazado(EstadoBase):
    def nombre_estado(self) -> str:
        return "RECHAZADO"

    def transicion(self) -> str | None:
        return None
