from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from schema import engine, Medico, Paciente, Turno


Session = sessionmaker(bind=engine)
session = Session()


# --------------------------
# 1. FILTER CON ==
# Médicos que están activos
# --------------------------

print("\n--- MEDICOS ACTIVOS ---")

medicos_activos = (
    session.query(Medico)
    .filter(Medico.activo == True)
    .all()
)

for medico in medicos_activos:
    print(medico.nombre, medico.apellido)


# -------------------------------
# 2. FILTER CON >
# Pacientes cuyo ID es mayor a 5
# -------------------------------

print("\n--- PACIENTES CON ID MAYOR A 5 ---")

pacientes = (
    session.query(Paciente)
    .filter(Paciente.id > 5)
    .all()
)

for paciente in pacientes:
    print(paciente.id, paciente.nombre, paciente.apellido)


# -------------------------------
# 3. FILTER CON !=
# Turnos que no están cancelados
# -------------------------------

print("\n--- TURNOS NO CANCELADOS ---")

turnos = (
    session.query(Turno)
    .filter(Turno.estado != "Cancelado")
    .all()
)

for turno in turnos:
    print(turno.id, turno.fecha_hora, turno.estado)


# -----------------------------
# 4. CONSULTA CON or_()
# Pacientes con OSDE o Galeno
# -----------------------------

print("\n--- PACIENTES CON OSDE O GALENO ---")

pacientes_obra_social = (
    session.query(Paciente)
    .filter(
        or_(
            Paciente.obra_social == "OSDE",
            Paciente.obra_social == "Galeno"
        )
    )
    .all()
)

for paciente in pacientes_obra_social:
    print(
        paciente.nombre,
        paciente.apellido,
        "-",
        paciente.obra_social
    )


# ------------------------------------
# 5. CONSULTA CON startswith()
# Médicos cuyo nombre comienza con M
# ------------------------------------

print("\n--- MEDICOS CUYO NOMBRE EMPIEZA CON M ---")

medicos_m = (
    session.query(Medico)
    .filter(Medico.nombre.startswith("M"))
    .all()
)

for medico in medicos_m:
    print(medico.nombre, medico.apellido)


# ------------------------------
# 6. order_by().first()
# Turno con la fecha más lejana
# ------------------------------

print("\n--- TURNO CON FECHA MAS LEJANA ---")

ultimo_turno = (
    session.query(Turno)
    .order_by(Turno.fecha_hora.desc())
    .first()
)

if ultimo_turno:
    print(
        ultimo_turno.id,
        ultimo_turno.fecha_hora,
        ultimo_turno.motivo,
        ultimo_turno.estado
    )


session.close()
