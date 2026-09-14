from __future__ import annotations

from typing import TYPE_CHECKING

from .suscriptor import Suscriptor

if TYPE_CHECKING:
    from candidato import Candidato

_ESTADOS_RELEVANTES: set[str] = {"OFERTA", "CONTRATADO"}


class SuscriptorGerente(Suscriptor):
    def __init__(
        self,
        _email_gerente: str
    ) -> None:
        self._email_gerente: str = _email_gerente

    def notificar(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        if nombre_estado not in _ESTADOS_RELEVANTES:
            return
        print(
            f"[Gerente] {candidato.nombre} pasó a estado {nombre_estado}. "
            f"Enviando notificación a {self._email_gerente}."
        )
