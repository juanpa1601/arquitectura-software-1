# Arquitectura de Software 1

Ejercicios de la materia Arquitectura de Software, en Python. Cada proyecto parte de un diseño simple y se refactoriza por versiones aplicando principios SOLID y patrones de diseño.

## Tecnologías

- Python 3.10 o superior (solo biblioteca estándar)
- pytest (para las pruebas de `notifi_core`)

## Proyectos

### `offer_core/`: motor de descuentos del checkout

Calcula el descuento de un pedido según el tipo de cliente (nuevo, frecuente, VIP, corporativo) y la categoría del producto.

| Versión | Qué cambia |
|---|---|
| `v1` | Código inicial: un único método con `if/elif` anidados (el "antes" del refactor) |
| `v3` | SRP y OCP: cada regla es una clase que implementa `DiscountRule`; el servicio solo conoce la abstracción |
| `v4` | El mismo diseño organizado en paquetes (`domain/`, `rules/`, `services/`) más una factory de reglas |

### `hire_core/`: proceso de contratación de candidatos

Gestiona el ciclo de un candidato: aplicado → entrevista → prueba técnica → oferta → verificación de referencias → contratado (o rechazado).

| Versión | Qué agrega |
|---|---|
| `v2` | **State**: una clase por estado con sus transiciones válidas |
| `v3` | **Observer**: al cambiar de estado se notifica a reclutador, gerente, nómina y portal del candidato |
| `v4` | **Command**: cada transición queda registrada como comando con usuario y fecha, y se puede deshacer la última operación; incluye un registro de auditoría |

### `notifi_core/`: sistema de notificaciones

Decide por qué canal (email, push o SMS) notificar un evento según el rol del destinatario.

- **Adapter**: `EmailAdapter`, `PushAdapter` y `SmsAdapter` envuelven SDKs simulados detrás de `NotificationSender`.
- **Factory**: `NotificationFactory` crea la regla adecuada a partir de una configuración por evento y rol.
- **Decorator**: `NotificationDecorator` agrega reintentos y logging al envío.
- 15 pruebas con pytest.

## Cómo ejecutarlo

Cada versión es independiente y se ejecuta desde su carpeta:

```bash
cd offer_core/v4 && python app.py
cd hire_core/v4 && python app.py
cd notifi_core && python app.py
```

Pruebas de `notifi_core`:

```bash
cd notifi_core
pip install pytest
python -m pytest
```

Probado localmente con Python 3.14: todos los `app.py` corren y las 15 pruebas pasan. `offer_core/v1` solo define las clases y no imprime nada, porque es el código de partida del ejercicio.
