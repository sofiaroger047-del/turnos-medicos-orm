from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Especialidad(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)

    medicos = relationship("Medico", back_populates="especialidad")


class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    especialidad_id = Column(
        Integer,
        ForeignKey("especialidades.id"),
        nullable=False
    )
    activo = Column(Boolean, default=True)

    especialidad = relationship("Especialidad", back_populates="medicos")
    turnos = relationship("Turno", back_populates="medico")


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, nullable=False)
    obra_social = Column(String)

    turnos = relationship("Turno", back_populates="paciente")


class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=False)
    estado = Column(String, nullable=False)

    paciente_id = Column(
        Integer,
        ForeignKey("pacientes.id"),
        nullable=False
    )

    medico_id = Column(
        Integer,
        ForeignKey("medicos.id"),
        nullable=False
    )

    paciente = relationship("Paciente", back_populates="turnos")
    medico = relationship("Medico", back_populates="turnos")


engine = create_engine("sqlite:///turnos_medicos.db")

Base.metadata.create_all(engine)

print("Base de datos y tablas creadas correctamente.")
