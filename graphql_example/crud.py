import graphene
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Controller, SystemUnderTest, engine
from .schema import SystemUnderTestType

Session = scoped_session(sessionmaker(bind=engine))


class CreateController(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    fqdn = graphene.String()
    location = graphene.String()
    suts = graphene.List(SystemUnderTestType)

    def resolve_suts(self, controller, args, info):
        return controller.suts.all()

    class Arguments:
        name = graphene.String()
        fqdn = graphene.String()
        location = graphene.String()

    def mutate(self, info, name, fqdn, location):
        session = Session()
        controller = Controller(name=name, fqdn=fqdn, location=location)
        session.add(controller)
        session.commit()

        return CreateController(
            id=controller.id,
            name=controller.name,
            fqdn=controller.fqdn,
            location=controller.location,
        )


class CreateSystemUnderTest(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    ip = graphene.String()
    controllerID = graphene.Int()

    class Arguments:
        name = graphene.String()
        ip = graphene.String()
        controllerID = graphene.Int()

    def mutate(self, info, name, ip, controllerID):
        session = Session()
        systemUnderTest = SystemUnderTest(name=name, ip=ip, controllerID=controllerID)
        session.add(systemUnderTest)
        session.commit()

        return CreateSystemUnderTest(
            id=systemUnderTest.id,
            name=systemUnderTest.name,
            ip=systemUnderTest.ip,
            controllerID=systemUnderTest.controllerID,
        )
