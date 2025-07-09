from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Date, DECIMAL
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
import uuid

from app.database import Base


class AssistanceCategory(enum.Enum):
    pasajes = "pasajes"
    monetaria = "monetaria"
    gestiones = "gestiones"
    medicamentos = "medicamentos"
    empleo = "empleo"
    otros = "otros"


class AssistanceStatus(enum.Enum):
    solicitada = "solicitada"
    en_proceso = "en_proceso"
    completada = "completada"
    cancelada = "cancelada"


class AssistanceType(Base):
    __tablename__ = "assistance_types"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String)
    category = Column(Enum(AssistanceCategory), nullable=False)
    requires_amount = Column(Boolean, default=False)
    default_amount = Column(DECIMAL(10, 2))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    assistances = relationship("Assistance", back_populates="assistance_type")


class Assistance(Base):
    __tablename__ = "assistances"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    assistance_type_id = Column(Integer, ForeignKey("assistance_types.id"), nullable=False)
    description = Column(String, nullable=False)
    amount = Column(DECIMAL(10, 2))
    currency = Column(String(10), default="COP")
    date_requested = Column(Date, nullable=False, server_default=func.current_date())
    date_completed = Column(Date)
    status = Column(Enum(AssistanceStatus), default=AssistanceStatus.solicitada, nullable=False)
    notes = Column(String)
    supporting_documents = Column(JSONB)
    beneficiary_signature = Column(String)
    authorized_by = Column(Integer, ForeignKey("users.id"))
    headquarters_id = Column(Integer, ForeignKey("political_headquarters.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    completed_by = Column(Integer, ForeignKey("users.id"))

    # Relationships
    person = relationship("Person", back_populates="assistances")
    assistance_type = relationship("AssistanceType", back_populates="assistances")
    creator = relationship("User", back_populates="created_assistances", foreign_keys=[created_by])
    observations = relationship("Observation", back_populates="assistance")