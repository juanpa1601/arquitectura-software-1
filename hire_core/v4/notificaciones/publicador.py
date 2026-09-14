from __future__ import annotations

from typing import TYPE_CHECKING

from .suscriptor import Suscriptor

if TYPE_CHECKING:
    from candidato import Candidato


class Publicador:
    def __init__(self) -> None:
        self._suscriptores: list[Suscriptor] = []

    def agregar_suscriptor(
        self,
        suscriptor: Suscriptor
    ) -> None:
        self._suscriptores.append(suscriptor)

    def notificar_suscriptores(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        for suscriptor in self._suscriptores:
            suscriptor.notificar(
                candidato, 
                nombre_estado
            )
