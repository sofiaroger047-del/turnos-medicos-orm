# Turnos Médicos ORM

Trabajo práctico integrador de ORM y bases de datos.

## Caso elegido

Caso G — Turnos médicos.

El sistema permite gestionar:

- Especialidades
- Médicos
- Pacientes
- Turnos

## Integrante

- Camila Cori Angola

## Tecnologías utilizadas

- Python
- SQLAlchemy
- SQLite

## Archivos del proyecto

- `schema.py`: contiene los modelos, relaciones y creación de la base de datos.
- `seed.py`: carga los datos iniciales.
- `consultas.py`: contiene las consultas realizadas con SQLAlchemy.
- `turnos_medicos.db`: base de datos SQLite.

## Instalación

Crear y activar un entorno virtual.
```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar SQLAlchemy
```bash
pip install sqlalquemy
```

## Ejecución

Primero ejecutar
```bash
python3 schema.py
```

Luego cargar los datos
```bash
python3 seed.py
```

Finalmente ejecutar las consultas
```bash
python3 consultas.py
```

## Base de Datos

El proyecto utiliza SQLite.

Las tablas utilizadas son:
- Especialidad
- Medico
- Paciente
- Turno
