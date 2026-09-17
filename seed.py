from datetime import datetime
from sqlalchemy.orm import sessionmaker

from schema import engine, Especialidad, Medico, Paciente, Turno


Session = sessionmaker(bind=engine)
session = Session()


# ---------------
# ESPECIALIDADES
# ---------------

especialidades = [
    Especialidad(nombre="Cardiología", descripcion="Enfermedades del corazón"),
    Especialidad(nombre="Pediatría", descripcion="Atención médica infantil"),
    Especialidad(nombre="Dermatología", descripcion="Enfermedades de la piel"),
    Especialidad(nombre="Traumatología", descripcion="Lesiones y sistema musculoesquelético"),
    Especialidad(nombre="Neurología", descripcion="Enfermedades del sistema nervioso"),
    Especialidad(nombre="Oftalmología", descripcion="Salud y enfermedades de los ojos"),
    Especialidad(nombre="Ginecología", descripcion="Salud reproductiva femenina"),
    Especialidad(nombre="Clínica Médica", descripcion="Atención médica general"),
    Especialidad(nombre="Otorrinolaringología", descripcion="Oído, nariz y garganta"),
    Especialidad(nombre="Endocrinología", descripcion="Sistema hormonal y metabolismo"),
]

session.add_all(especialidades)
session.commit()


# --------
# MEDICOS
# --------

medicos = [
    Medico(
        nombre="Laura",
        apellido="Fernández",
        matricula="MED001",
        especialidad=especialidades[0],
        activo=True,
    ),
    Medico(
        nombre="Carlos",
        apellido="Gómez",
        matricula="MED002",
        especialidad=especialidades[1],
        activo=True,
    ),
    Medico(
        nombre="Mariana",
        apellido="López",
        matricula="MED003",
        especialidad=especialidades[2],
        activo=False,
    ),
    Medico(
        nombre="Javier",
        apellido="Rodríguez",
        matricula="MED004",
        especialidad=especialidades[3],
        activo=True,
    ),
    Medico(
        nombre="Andrea",
        apellido="Martínez",
        matricula="MED005",
        especialidad=especialidades[4],
        activo=True,
    ),
    Medico(
        nombre="Diego",
        apellido="Sánchez",
        matricula="MED006",
        especialidad=especialidades[5],
        activo=False,
    ),
    Medico(
        nombre="Valeria",
        apellido="Romero",
        matricula="MED007",
        especialidad=especialidades[6],
        activo=True,
    ),
    Medico(
        nombre="Martín",
        apellido="Pérez",
        matricula="MED008",
        especialidad=especialidades[7],
        activo=True,
    ),
    Medico(
        nombre="Natalia",
        apellido="Torres",
        matricula="MED009",
        especialidad=especialidades[8],
        activo=True,
    ),
    Medico(
        nombre="Federico",
        apellido="Díaz",
        matricula="MED010",
        especialidad=especialidades[9],
        activo=False,
    ),
]

session.add_all(medicos)
session.commit()


# ----------
# PACIENTES
# ----------

pacientes = [
    Paciente(nombre="Ana", apellido="Suárez", dni="40111222", obra_social="OSDE"),
    Paciente(nombre="Bruno", apellido="Molina", dni="38999111", obra_social="Swiss Medical"),
    Paciente(nombre="Camila", apellido="Acosta", dni="42777888", obra_social="Galeno"),
    Paciente(nombre="Daniel", apellido="Ruiz", dni="36555444", obra_social=None),
    Paciente(nombre="Elena", apellido="Castro", dni="41999888", obra_social="Medifé"),
    Paciente(nombre="Franco", apellido="Silva", dni="39777111", obra_social="OSDE"),
    Paciente(nombre="Gabriela", apellido="Herrera", dni="43222111", obra_social=None),
    Paciente(nombre="Hugo", apellido="Navarro", dni="35111222", obra_social="PAMI"),
    Paciente(nombre="Irene", apellido="Vega", dni="44555666", obra_social="Galeno"),
    Paciente(nombre="Juan", apellido="Ramos", dni="40888777", obra_social="Swiss Medical"),
]

session.add_all(pacientes)
session.commit()


# -------
# TURNOS
# -------

turnos = [
    Turno(
        fecha_hora=datetime(2026, 9, 20, 9, 0),
        motivo="Control general",
        estado="Pendiente",
        paciente=pacientes[0],
        medico=medicos[7],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 20, 10, 30),
        motivo="Dolor de pecho",
        estado="Confirmado",
        paciente=pacientes[1],
        medico=medicos[0],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 21, 8, 30),
        motivo="Consulta pediátrica",
        estado="Pendiente",
        paciente=pacientes[2],
        medico=medicos[1],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 21, 11, 0),
        motivo="Dolor de rodilla",
        estado="Confirmado",
        paciente=pacientes[3],
        medico=medicos[3],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 22, 14, 0),
        motivo="Migrañas frecuentes",
        estado="Pendiente",
        paciente=pacientes[4],
        medico=medicos[4],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 22, 16, 30),
        motivo="Control de visión",
        estado="Cancelado",
        paciente=pacientes[5],
        medico=medicos[5],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 23, 9, 30),
        motivo="Control ginecológico",
        estado="Confirmado",
        paciente=pacientes[6],
        medico=medicos[6],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 23, 12, 0),
        motivo="Dolor de garganta",
        estado="Pendiente",
        paciente=pacientes[7],
        medico=medicos[8],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 24, 15, 0),
        motivo="Control hormonal",
        estado="Confirmado",
        paciente=pacientes[8],
        medico=medicos[9],
    ),
    Turno(
        fecha_hora=datetime(2026, 9, 25, 10, 0),
        motivo="Chequeo cardiológico",
        estado="Atendido",
        paciente=pacientes[9],
        medico=medicos[0],
    ),
]

session.add_all(turnos)
session.commit()


session.close()

print("Datos cargados correctamente.")
