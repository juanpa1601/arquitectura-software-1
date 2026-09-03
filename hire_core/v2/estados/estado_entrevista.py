from __future__ import annotations

from typing import Optional

from .estado_base import EstadoBase


class EstadoEntrevista(EstadoBase):
    def nombre_estado(self) -> str:
        return "ENTREVISTA"

    def transicion(self) -> Optional[str]:
        return "PRUEBA_TECNICA"
