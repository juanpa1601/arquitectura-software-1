from __future__ import annotations

from typing import Optional

from .estado_base import EstadoBase


class EstadoOferta(EstadoBase):
    def nombre_estado(self) -> str:
        return "OFERTA"

    def transicion(self) -> Optional[str]:
        return "VERIFICACION_REFERENCIAS"
