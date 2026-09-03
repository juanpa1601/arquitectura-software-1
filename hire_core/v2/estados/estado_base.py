from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Optional

from .estado import Estado

if TYPE_CHECKING:
    from gestor_de_candidato import GestorDeCandidato


class EstadoBase(Estado):
    _registro_estados: dict[str, "EstadoBase"] = {}

    @abstractmethod
    def nombre_estado(self) -> str:
        ...

    @abstractmethod
    def transicion(self) -> Optional[str]:
        ...

    def actualizar(self, gestor_candidato: GestorDeCandidato) -> None:
        siguiente_estado = EstadoBase._registro_estados[self.transicion()]
        gestor_candidato._actualizar_estado(siguiente_estado)

    def rechazar(self, gestor_candidato: GestorDeCandidato) -> None:
        estado_rechazado = EstadoBase._registro_estados["RECHAZADO"]
        gestor_candidato._actualizar_estado(estado_rechazado)
