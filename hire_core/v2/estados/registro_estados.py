from __future__ import annotations

from .estado_base import EstadoBase
from .estado_aplicado import EstadoAplicado
from .estado_entrevista import EstadoEntrevista
from .estado_prueba_tecnica import EstadoPruebaTecnica
from .estado_oferta import EstadoOferta
from .estado_verificacion_referencias import EstadoVerificacionReferencias
from .estado_contratado import EstadoContratado
from .estado_rechazado import EstadoRechazado

_estados_a_registrar: tuple[EstadoBase, ...] = (
    EstadoAplicado(),
    EstadoEntrevista(),
    EstadoPruebaTecnica(),
    EstadoOferta(),
    EstadoVerificacionReferencias(),
    EstadoContratado(),
    EstadoRechazado(),
)

for _estado in _estados_a_registrar:
    EstadoBase._registro_estados[_estado.nombre_estado()] = _estado
