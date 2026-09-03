from __future__ import annotations

from typing import Optional

from .estado_base import EstadoBase


class EstadoVerificacionReferencias(EstadoBase):
    def nombre_estado(self) -> str:
        return "VERIFICACION_REFERENCIAS"

    def transicion(self) -> Optional[str]:
        return "CONTRATADO"
