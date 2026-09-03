from __future__ import annotations

from .estado_base import EstadoBase


class EstadoVerificacionReferencias(EstadoBase):
    def nombre_estado(self) -> str:
        return "VERIFICACION_REFERENCIAS"

    def transicion(self) -> str | None:
        return "CONTRATADO"
