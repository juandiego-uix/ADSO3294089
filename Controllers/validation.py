from datetime import datetime
from numbers import Real


def validate_payload(data, required, integer_fields=(), decimal_fields=(),
                     date_fields=(), ranges=None, defaults=None):
    if not isinstance(data, dict):
        return None, "JSON invalido"

    payload = dict(data)
    for field, value in (defaults or {}).items():
        payload.setdefault(field, value)

    missing = [
        field for field in required
        if field not in payload or payload[field] is None or payload[field] == ""
    ]
    if missing:
        return None, f"Faltan parametros: {missing}"

    for field in integer_fields:
        value = payload[field]
        if isinstance(value, bool) or not isinstance(value, int):
            return None, f"El parametro {field} debe ser entero"
        if value <= 0:
            return None, f"El parametro {field} debe ser mayor que cero"

    for field in decimal_fields:
        value = payload[field]
        if isinstance(value, bool) or not isinstance(value, Real):
            return None, f"El parametro {field} debe ser numerico"

    for field in date_fields:
        try:
            datetime.strptime(payload[field], "%Y-%m-%d")
        except (TypeError, ValueError):
            return None, f"El parametro {field} debe tener formato AAAA-MM-DD"

    for field, (minimum, maximum) in (ranges or {}).items():
        value = payload[field]
        if value < minimum or (maximum is not None and value > maximum):
            return None, f"El parametro {field} esta fuera de rango"

    return payload, None
