from sqlalchemy import Column, String, Date

from database import Base

# Criando a class Pessoa que será usada para criar a tabela no banco de dados
class Person(Base):
    __tablename__ = "Person" # Nome da tabela
    
    CPF = Column(String(50), primary_key=True, index=True)
    primeiro_nome = Column(String(75), nullable=False)
    segundo_nome = Column(String(75), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    email = Column(String(200))
    