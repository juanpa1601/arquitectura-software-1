from __future__ import annotations

from auditoria import Auditoria
from candidato import Candidato
from estados import EstadoBase
from gestor_de_candidato import GestorDeCandidato
from notificaciones import (
    Publicador,
    SuscriptorReclutador,
    SuscriptorPortal,
    SuscriptorGerente,
    SuscriptorNomina,
)
from usuario import Usuario


def construir_publicador() -> Publicador:
    publicador: Publicador = Publicador()
    publicador.agregar_suscriptor(SuscriptorReclutador())
    publicador.agregar_suscriptor(SuscriptorPortal())
    publicador.agregar_suscriptor(SuscriptorGerente("gerente@hirecore.com"))
    publicador.agregar_suscriptor(SuscriptorNomina("nomina@hirecore.com"))
    return publicador


def construir_gestor() -> GestorDeCandidato:
    estado_inicial: EstadoBase = EstadoBase._registro_estados["APLICADO"]
    candidato: Candidato = Candidato(
        nombre="Ana Torres",
        email="ana.torres@example.com",
        reclutador_email="reclutador@hirecore.com",
    )
    return GestorDeCandidato(
        estado_inicial,
        candidato,
        construir_publicador(),
        Auditoria(),
    )


if __name__ == "__main__":
    usuario: Usuario = Usuario("Carla Méndez")

    gestor: GestorDeCandidato = construir_gestor()
    print(gestor.estado_actual.nombre_estado())
    for _ in range(5):
        gestor.avanzar(usuario)
        print(gestor.estado_actual.nombre_estado())

    gestor_rechazado: GestorDeCandidato = construir_gestor()
    gestor_rechazado.avanzar(usuario)
    gestor_rechazado.avanzar(usuario)
    gestor_rechazado.rechazar(usuario)
    print(gestor_rechazado.estado_actual.nombre_estado())

    gestor_rechazado.deshacer(usuario)
    print(gestor_rechazado.estado_actual.nombre_estado())
    gestor_rechazado.deshacer(usuario)
