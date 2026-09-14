from __future__ import annotations


class Candidato:
    def __init__(
        self,
        nombre: str,
        email: str,
        reclutador_email: str,
    ) -> None:
        self._estado: str = "APLICADO"
        self._nombre: str = nombre
        self._email: str = email
        self._reclutador_email: str = reclutador_email

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(
        self,
        valor: str
    ) -> None:
        self._estado = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email

    @property
    def reclutador_email(self) -> str:
        return self._reclutador_email
