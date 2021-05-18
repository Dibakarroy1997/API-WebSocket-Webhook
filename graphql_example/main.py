import graphene
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route

from .crud import CreateController, CreateSystemUnderTest, Session
from .models import Controller, SystemUnderTest
from .schema import ControllerType, SystemUnderTestType


class Mutation(graphene.ObjectType):
    create_controller = CreateController.Field()
    create_sut = CreateSystemUnderTest.Field()


class Query(graphene.ObjectType):
    controller = graphene.List(ControllerType, name=graphene.String())
    sut = graphene.List(SystemUnderTestType, name=graphene.String())

    def resolve_controller(self, info, name):
        session = Session()
        controller = session.query(Controller).filter(Controller.name == name).all()
        return controller

    def resolve_sut(self, info, name):
        session = Session()
        systemUnderTest = (
            session.query(SystemUnderTest).filter(SystemUnderTest.name == name).all()
        )
        return systemUnderTest


routes = [
    Route("/", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))
]

app = Starlette(routes=routes)

# uvicorn graphql_example.main:app --reload
