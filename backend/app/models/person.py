from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
import uuid

from app.database import Base


class GenderType(enum.Enum):
    F = "F"
    M = "M"


class PoliticalRole(enum.Enum):
    simpatizante = "simpatizante"
    lider = "lider"
    voluntario = "voluntario"


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    referido_por = Column(String(100))
    cedula = Column(String(20), unique=True, nullable=False, index=True)
    fecha_registro = Column(Date, nullable=False, server_default=func.current_date())
    ciudad = Column(String(100), nullable=False)
    sexo = Column(Enum(GenderType), nullable=False)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    cedula_expedida_en = Column(String(100))
    fecha_nacimiento = Column(Date)
    estado_civil = Column(String(50))
    hijos = Column(Integer, default=0)
    profesion_oficio = Column(String(100))
    tiene_correo = Column(Boolean, default=False)
    correo_electronico = Column(String(100))
    telefono_domicilio = Column(String(20))
    telefono_oficina = Column(String(20))
    celular_1 = Column(String(20))
    celular_2 = Column(String(20))
    whatsapp = Column(String(20))
    direccion = Column(String)
    barrio = Column(String(100))
    vereda_corregimiento = Column(String(100))
    rol_politico = Column(Enum(PoliticalRole), default=PoliticalRole.simpatizante, nullable=False)
    lider_id = Column(Integer, ForeignKey("people.id"))
    headquarters_id = Column(Integer, ForeignKey("political_headquarters.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    lider = relationship("Person", remote_side=[id])
    referidos = relationship("Person", back_populates="lider")
    creator = relationship("User", back_populates="created_people")
    assistances = relationship("Assistance", back_populates="person")
    observations = relationship("Observation", back_populates="person")