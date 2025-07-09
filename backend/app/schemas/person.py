from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime, date
from app.models.person import GenderType, PoliticalRole


class PersonBase(BaseModel):
    referido_por: Optional[str] = None
    cedula: str
    ciudad: str
    sexo: GenderType
    nombres: str
    apellidos: str
    cedula_expedida_en: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    estado_civil: Optional[str] = None
    hijos: int = 0
    profesion_oficio: Optional[str] = None
    tiene_correo: bool = False
    correo_electronico: Optional[str] = None
    telefono_domicilio: Optional[str] = None
    telefono_oficina: Optional[str] = None
    celular_1: Optional[str] = None
    celular_2: Optional[str] = None
    whatsapp: Optional[str] = None
    direccion: Optional[str] = None
    barrio: Optional[str] = None
    vereda_corregimiento: Optional[str] = None
    rol_politico: PoliticalRole = PoliticalRole.simpatizante
    lider_id: Optional[int] = None
    headquarters_id: Optional[int] = None


class PersonCreate(PersonBase):
    pass


class PersonUpdate(BaseModel):
    referido_por: Optional[str] = None
    ciudad: Optional[str] = None
    sexo: Optional[GenderType] = None
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    cedula_expedida_en: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    estado_civil: Optional[str] = None
    hijos: Optional[int] = None
    profesion_oficio: Optional[str] = None
    tiene_correo: Optional[bool] = None
    correo_electronico: Optional[str] = None
    telefono_domicilio: Optional[str] = None
    telefono_oficina: Optional[str] = None
    celular_1: Optional[str] = None
    celular_2: Optional[str] = None
    whatsapp: Optional[str] = None
    direccion: Optional[str] = None
    barrio: Optional[str] = None
    vereda_corregimiento: Optional[str] = None
    rol_politico: Optional[PoliticalRole] = None
    lider_id: Optional[int] = None
    headquarters_id: Optional[int] = None
    is_active: Optional[bool] = None


class PersonResponse(PersonBase):
    id: int
    uuid: UUID4
    fecha_registro: date
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PersonSearch(BaseModel):
    search_term: str
    limit: int = 10
    offset: int = 0