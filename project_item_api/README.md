## Proyecto de Ítems - Backend

Este proyecto es un ejemplo simple de uso de FastAPI para crear un CRUD básico de ítems.

## Inicialización del proyecto

### Sincronizar las dependencias

Si descargas el proyecto, necesitas sincronizar las dependencias:

```bash
uv sync
```

## Estructura del proyecto

```
pyproject.toml
README.md
uv.lock
src/
    __init__.py
    constants.py
    main.py
    routes/
        __init__.py
        item_routes.py
    schemas/
        __init__.py
        item_schemas.py
test/
    __init__.py
    test_item_routes.py
    test_item_schemas.py
    test_main.py
```

- `src/`: Código fuente principal.
  - `main.py`: Punto de entrada de la API.
  - `routes/`: Rutas/endpoints de la API.
  - `schemas/`: Esquemas y validaciones de datos.
  - `constants.py`: Constantes usadas en la API.
- `test/`: Pruebas unitarias y de integración.
- `pyproject.toml`, `uv.lock`: Archivos de configuración y dependencias.

## Ejecutar el proyecto

Una vez instaladas las dependencias, puedes iniciar el backend con:

```bash
uv run fastapi dev src/main.py
```

