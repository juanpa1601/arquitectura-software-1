from __future__ import annotations

from .estado_base import EstadoBase


class EstadoContratado(EstadoBase):
    def nombre_estado(self) -> str:
        return "CONTRATADO"

    def transicion(self) -> str | None:
        raise NotImplementedError
