from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base


class PoliticalHeadquarter(Base):
    __tablename__ = "political_headquarters"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String, nullable=False)
    city = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    manager_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    people = relationship("Person", back_populates="headquarters")
    assistances = relationship("Assistance", back_populates="headquarters")
