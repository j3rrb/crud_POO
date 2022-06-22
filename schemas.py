from datetime import date
from pydantic import BaseModel

# Criando a classe Pessoa que será utilizada para realizar a tipagem de dados
class Person(BaseModel):
    CPF: str
    primeiro_nome: str
    segundo_nome: str
    data_nascimento: date
    email: str | None

    class Config:
        orm_mode = True
