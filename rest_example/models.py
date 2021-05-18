from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Controller(Base):
    __tablename__ = "controllers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    fqdn = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)

    suts = relationship("SystemUnderTest")


class SystemUnderTest(Base):
    __tablename__ = "suts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ip = Column(String)
    controllerID = Column(Integer, ForeignKey("controllers.id"), nullable=False)
