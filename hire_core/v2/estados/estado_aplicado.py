from __future__ import annotations

from .estado_base import EstadoBase


class EstadoAplicado(EstadoBase):
    def nombre_estado(self) -> str:
        return "APLICADO"

    def transicion(self) -> str | None:
        return "ENTREVISTA"
