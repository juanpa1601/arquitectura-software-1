from __future__ import annotations

from candidato import Candidato
from estados import EstadoBase
from gestor_de_candidato import GestorDeCandidato


def construir_gestor() -> GestorDeCandidato:
    estado_inicial = EstadoBase._registro_estados["APLICADO"]
    return GestorDeCandidato(estado_inicial, Candidato())


if __name__ == "__main__":
    gestor = construir_gestor()
    print(gestor.estado_actual.nombre_estado())
    for _ in range(5):
        gestor.avanzar()
        print(gestor.estado_actual.nombre_estado())

    gestor_rechazado = construir_gestor()
    gestor_rechazado.avanzar()
    gestor_rechazado.avanzar()
    gestor_rechazado.rechazar()
    print(gestor_rechazado.estado_actual.nombre_estado())
