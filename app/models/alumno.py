from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .profesor import Profesor

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Alumno(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apedillo_1 = Column(String, index=True)
    apedillo_2 = Column(String, index=True)
    edad = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    # hashed_password = Column(String, nullable=False)
    # is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)
    # asignatura = relationship("Item", back_populates="owner")