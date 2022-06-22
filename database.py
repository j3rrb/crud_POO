from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3360/crud"

# Cria a conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria a sessão, que é uma classe que manipula o banco de dados através do ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Forma que serão criadas as tabelas (declarativa ou imperativa)
Base = declarative_base()
