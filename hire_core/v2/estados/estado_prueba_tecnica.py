from __future__ import annotations

from typing import Optional

from .estado_base import EstadoBase


class EstadoPruebaTecnica(EstadoBase):
    def nombre_estado(self) -> str:
        return "PRUEBA_TECNICA"

    def transicion(self) -> Optional[str]:
        return "OFERTA"
