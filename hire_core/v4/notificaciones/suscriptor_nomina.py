from __future__ import annotations

from typing import TYPE_CHECKING

from .suscriptor import Suscriptor

if TYPE_CHECKING:
    from candidato import Candidato


class SuscriptorNomina(Suscriptor):
    def __init__(
        self,
        _email_nomina: str
    ) -> None:
        self._email_nomina: str = _email_nomina

    def notificar(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        if nombre_estado != "CONTRATADO":
            return
        print(
            f"[Nómina] {candidato.nombre} pasó a estado {nombre_estado}. "
            f"Enviando notificación a {self._email_nomina}."
        )
