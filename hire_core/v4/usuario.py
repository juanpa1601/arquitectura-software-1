from __future__ import annotations


class Usuario:
    def __init__(
        self,
        nombre: str
    ) -> None:
        self._nombre: str = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
