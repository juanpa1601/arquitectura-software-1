from __future__ import annotations

from datetime import datetime
from typing import Optional

from auditoria import Auditoria
from candidato import Candidato
from comando import Comando
from estados import Estado
from notificaciones import Publicador
from usuario import Usuario


class GestorDeCandidato:
    def __init__(
        self,
        estado_inicial: Estado,
        candidato: Candidato,
        publicador: Publicador,
        auditoria: Auditoria
    ) -> None:
        self._estado_actual: Estado = estado_inicial
        self._candidato: Candidato = candidato
        self._publicador: Publicador = publicador
        self._auditoria: Auditoria = auditoria
        self._ultimo_comando: Optional[Comando] = None

    @property
    def estado_actual(self) -> Estado:
        return self._estado_actual

    @property
    def candidato(self) -> Candidato:
        return self._candidato

    def _actualizar_estado(
        self,
        nuevo_estado: Estado,
        usuario: Usuario
    ) -> None:
        """Uso interno: solo debe ser invocado por los colaboradores Estado/EstadoBase."""
        transicion_valida: bool = nuevo_estado.nombre_estado() in (
            self._estado_actual.transicion(),
            "RECHAZADO",
        )
        if not transicion_valida:
            raise ValueError(
                f"Transición inválida: {self._estado_actual.nombre_estado()} -> {nuevo_estado.nombre_estado()}"
            )
        comando: Comando = Comando(
            usuario=usuario,
            candidato=self._candidato,
            estado_anterior=self._estado_actual,
            estado_nuevo=nuevo_estado,
            timestamp=datetime.now(),
        )
        self._ultimo_comando = comando
        self._auditoria.registrar(comando)
        self._estado_actual = nuevo_estado
        self._candidato.estado = nuevo_estado.nombre_estado()
        self._notificar_cambio(nuevo_estado.nombre_estado())

    def _notificar_cambio(
        self,
        nuevo_estado: str
    ) -> None:
        self._publicador.notificar_suscriptores(
            self._candidato,
            nuevo_estado
        )

    def avanzar(
        self,
        usuario: Usuario
    ) -> None:
        if self._estado_actual.transicion() is None:
            print(
                f"Operación inválida: el candidato ya está en un estado terminal "
                f"({self._estado_actual.nombre_estado()}) y no puede avanzar."
            )
            return
        self._estado_actual.actualizar(self, usuario)

    def rechazar(
        self,
        usuario: Usuario
    ) -> None:
        self._estado_actual.rechazar(self, usuario)

    def deshacer(
        self,
        usuario: Usuario
    ) -> None:
        if self._ultimo_comando is None:
            print("No hay ninguna operación para deshacer.")
            return
        estado_a_restaurar: Estado = self._ultimo_comando.estado_anterior
        estado_actual_antes_del_deshacer: Estado = self._estado_actual
        comando_deshacer: Comando = Comando(
            usuario=usuario,
            candidato=self._candidato,
            estado_anterior=estado_actual_antes_del_deshacer,
            estado_nuevo=estado_a_restaurar,
            timestamp=datetime.now(),
        )
        self._auditoria.registrar(comando_deshacer)
        self._estado_actual = estado_a_restaurar
        self._notificar_cambio(estado_a_restaurar.nombre_estado())
        self._ultimo_comando = None
