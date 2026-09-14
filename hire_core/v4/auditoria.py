from __future__ import annotations

from comando import Comando


class Auditoria:
    def __init__(self) -> None:
        self._registros: list[Comando] = []

    def registrar(
        self,
        comando: Comando
    ) -> None:
        self._registros.append(comando)
