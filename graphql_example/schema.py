from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import SystemUnderTest, Controller


class SystemUnderTestType(SQLAlchemyObjectType):
    class Meta:
        model = SystemUnderTest


class ControllerType(SQLAlchemyObjectType):
    class Meta:
        model = Controller
