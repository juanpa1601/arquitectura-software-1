"""Entidad de dominio: Event.

Es un value object simple (no involucra ningún patrón de diseño): existe
para darle al resto del pipeline una representación tipada de "algo que
ocurrió" en lugar de pasar un string suelto.
"""
from dataclasses import dataclass

@dataclass
class Event:
    type: str
