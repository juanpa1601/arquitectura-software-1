from __future__ import annotations

from typing import TYPE_CHECKING

from .suscriptor import Suscriptor

if TYPE_CHECKING:
    from candidato import Candidato


class SuscriptorReclutador(Suscriptor):
    def notificar(
        self,
        candidato: Candidato,
        nombre_estado: str
    ) -> None:
        print(
            f"[Reclutador] {candidato.nombre} pasó a estado {nombre_estado}. "
            f"Enviando notificación a {candidato.reclutador_email}."
        )
