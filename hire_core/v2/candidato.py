from __future__ import annotations


class Candidato:
    def __init__(self) -> None:
        self._estado: str = "APLICADO"

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(
        self, 
        valor: str
    ) -> None:
        self._estado = valor
