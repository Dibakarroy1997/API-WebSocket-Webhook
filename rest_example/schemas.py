from typing import List, Any

from pydantic import BaseModel


class SystemUnderTestBase(BaseModel):
    name: str
    ip: str


class SystemUnderTestCreate(SystemUnderTestBase):
    pass


class SystemUnderTest(SystemUnderTestBase):
    id: int

    class Config:
        orm_mode = True


class ControllerBase(BaseModel):
    name: str
    fqdn: str
    location: str


class ControllerCreate(ControllerBase):
    pass


class Controller(ControllerBase):
    id: int
    suts: List[SystemUnderTest] = []

    class Config:
        orm_mode = True
