from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/rest/controllers/", response_model=schemas.Controller)
def addController(controller: schemas.ControllerCreate, db: Session = Depends(get_db)):
    return crud.addController(db=db, controller=controller)


@app.get("/rest/controllers/", response_model=List[schemas.Controller])
def readControllers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.getControllers(db, skip=skip, limit=limit)
    return items


@app.post(
    "/rest/controllers/{controllerID}/suts/", response_model=schemas.SystemUnderTest
)
def addSutForController(
        controllerID: int, sut: schemas.SystemUnderTestCreate, db: Session = Depends(get_db)
):
    return crud.addSUTForController(db=db, sut=sut, controllerID=controllerID)


@app.get(
    "/rest/controllers/{controllerID}/suts/",
    response_model=List[schemas.SystemUnderTest],
)
def readSUTs(
        controllerID: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    items = crud.getSUTs(db, controllerID, skip, limit)
    return items

# uvicorn rest_example.main:app --reload
