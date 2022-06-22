from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
import schemas
import models

# Cria todas as tabelas a partir dos modelos
Base.metadata.create_all(engine)

# Instancia o FastAPI
app = FastAPI()


# Cria um generator para retornar a sessão que manipula o banco de dados através do ORM
def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()


# Busca todas as pessoas
@app.get("/people", response_model=List[schemas.Person])
def get_people(session: Session = Depends(get_session)):
    people = session.query(models.Person).all()

    return people


# Cria uma pessoa
@app.post("/people", status_code=status.HTTP_201_CREATED)
def create_person(data: schemas.Person, session: Session = Depends(get_session)):
    try:
        person_db = models.Person()

        person_db.CPF = data.CPF
        person_db.data_nascimento = data.data_nascimento
        person_db.primeiro_nome = data.primeiro_nome
        person_db.segundo_nome = data.segundo_nome
        person_db.email = data.email

        session.add(person_db)
        session.commit()
        session.refresh(person_db)

        return person_db

    except Exception:
        raise HTTPException(status_code=409)


# Busca uma pessoa
@app.get("/people/{cpf}")
def get_person(cpf: int, session: Session = Depends(get_session)):
    person = session.query(models.Person).get(cpf)

    if not person:
        raise HTTPException(status_code=404)

    return person


# Atualiza uma pessoa
@app.put("/people/{cpf}", response_model=schemas.Person)
def update_person(
    cpf: int, person: schemas.Person, session: Session = Depends(get_session)
):
    person_db = session.query(models.Person).get(cpf)

    if not person_db:
        raise HTTPException(status_code=404)

    person_db.CPF = person.CPF
    person_db.data_nascimento = person.data_nascimento
    person_db.primeiro_nome = person.primeiro_nome
    person_db.segundo_nome = person.segundo_nome
    person_db.email = person.email

    session.commit()

    return person_db


# Exclui uma pessoa
@app.delete("/people/{cpf}")
def delete_person(cpf: int, session: Session = Depends(get_session)):
    person_db = session.query(models.Person).get(cpf)

    if not person_db:
        raise HTTPException(status_code=404)

    session.delete(person_db)
    session.commit()