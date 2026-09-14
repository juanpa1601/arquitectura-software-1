from __future__ import annotations

from typing import TYPE_CHECKING

from .suscriptor import Suscriptor

if TYPE_CHECKING:
    from candidato import Candidato

_NOTA_INTERNA: str = "NOTA_INTERNA"


class SuscriptorPortal(Suscriptor):
    def notificar(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        if nombre_estado == _NOTA_INTERNA:
            return
        print(
            f"[Portal] {candidato.nombre} pasó a estado {nombre_estado}. "
            f"Enviando notificación a {candidato.email}."
        )
