from __future__ import annotations

from typing import Optional

from .estado_base import EstadoBase


class EstadoAplicado(EstadoBase):
    def nombre_estado(self) -> str:
        return "APLICADO"

    def transicion(self) -> Optional[str]:
        return "ENTREVISTA"
