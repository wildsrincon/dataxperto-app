from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
import uuid

from app.database import Base


class ObservationType(enum.Enum):
    general = "general"
    seguimiento = "seguimiento"
    alerta = "alerta"
    contacto = "contacto"


class PriorityType(enum.Enum):
    baja = "baja"
    media = "media"
    alta = "alta"


class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    assistance_id = Column(Integer, ForeignKey("assistances.id"))
    observation_type = Column(Enum(ObservationType), default=ObservationType.general, nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(String, nullable=False)
    priority = Column(Enum(PriorityType), default=PriorityType.media, nullable=False)
    is_private = Column(Boolean, default=False)
    reminder_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    person = relationship("Person", back_populates="observations")
    assistance = relationship("Assistance", back_populates="observations")
    creator = relationship("User", back_populates="created_observations")