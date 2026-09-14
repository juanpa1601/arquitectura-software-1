from __future__ import annotations

from .estado_base import EstadoBase


class EstadoEntrevista(EstadoBase):
    def nombre_estado(self) -> str:
        return "ENTREVISTA"

    def transicion(self) -> str | None:
        return "PRUEBA_TECNICA"
