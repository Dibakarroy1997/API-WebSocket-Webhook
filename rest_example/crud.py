from sqlalchemy.orm import Session

from . import models, schemas


def getControllers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Controller).offset(skip).limit(limit).all()


def addController(db: Session, controller: schemas.ControllerCreate):
    dbController = models.Controller(**controller.dict())
    db.add(dbController)
    db.commit()
    db.refresh(dbController)
    return dbController


def getSUTs(db: Session, controllerID: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.SystemUnderTest)
        .where(models.SystemUnderTest.controllerID == controllerID)
        .offset(skip)
        .limit(limit)
        .all()
    )


def addSUTForController(
    db: Session, sut: schemas.SystemUnderTestCreate, controllerID: int
):
    dbSUT = models.SystemUnderTest(**sut.dict(), controllerID=controllerID)
    db.add(dbSUT)
    db.commit()
    db.refresh(dbSUT)
    return dbSUT
