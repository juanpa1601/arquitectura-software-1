from __future__ import annotations

from datetime import datetime
from typing import Optional

from candidato import Candidato
from estados import Estado
from usuario import Usuario


class Comando:
    def __init__(
        self,
        usuario: Usuario,
        candidato: Candidato,
        estado_anterior: Estado,
        estado_nuevo: Estado,
        timestamp: Optional[datetime] = None
    ) -> None:
        self._usuario: Usuario = usuario
        self._candidato: Candidato = candidato
        self._estado_anterior: Estado = estado_anterior
        self._estado_nuevo: Estado = estado_nuevo
        self._timestamp: datetime = timestamp if timestamp is not None else datetime.now()

    @property
    def usuario(self) -> Usuario:
        return self._usuario

    @property
    def candidato(self) -> Candidato:
        return self._candidato

    @property
    def estado_anterior(self) -> Estado:
        return self._estado_anterior

    @property
    def estado_nuevo(self) -> Estado:
        return self._estado_nuevo

    @property
    def timestamp(self) -> datetime:
        return self._timestamp
