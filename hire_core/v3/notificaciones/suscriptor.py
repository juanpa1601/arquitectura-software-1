from __future__ import annotations

from abc import (
    ABC,
    abstractmethod
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from candidato import Candidato


class Suscriptor(ABC):
    @abstractmethod
    def notificar(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        ...
