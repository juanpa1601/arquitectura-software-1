from __future__ import annotations

from candidato import Candidato
from estados import Estado


class GestorDeCandidato:
    def __init__(
        self, 
        estado_inicial: Estado, 
        candidato: Candidato
    ) -> None:
        self._estado_actual: Estado = estado_inicial
        self._candidato: Candidato = candidato

    @property
    def estado_actual(self) -> Estado:
        return self._estado_actual

    @property
    def candidato(self) -> Candidato:
        return self._candidato

    def _actualizar_estado(
        self,
        nuevo_estado: Estado
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
        self._estado_actual = nuevo_estado
        self._candidato.estado = nuevo_estado.nombre_estado()

    def avanzar(self) -> None:
        if self._estado_actual.transicion() is None:
            print(
                f"Operación inválida: el candidato ya está en un estado terminal "
                f"({self._estado_actual.nombre_estado()}) y no puede avanzar."
            )
            return
        self._estado_actual.actualizar(self)

    def rechazar(self) -> None:
        self._estado_actual.rechazar(self)
