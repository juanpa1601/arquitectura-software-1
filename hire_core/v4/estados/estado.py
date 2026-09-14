from __future__ import annotations

from abc import (
    ABC,
    abstractmethod
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gestor_de_candidato import GestorDeCandidato
    from usuario import Usuario


class Estado(ABC):
    @abstractmethod
    def nombre_estado(self) -> str:
        ...

    @abstractmethod
    def transicion(self) -> str | None:
        ...

    @abstractmethod
    def actualizar(
        self,
        gestor_candidato: GestorDeCandidato,
        usuario: Usuario
    ) -> None:
        ...

    @abstractmethod
    def rechazar(
        self,
        gestor_candidato: GestorDeCandidato,
        usuario: Usuario
    ) -> None:
        ...
