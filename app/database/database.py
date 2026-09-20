from sqlalchemy import create_engine # da biblioteca sqlalchemy, importe a ferramenta create_engine #
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker cria sessões no banco, declarative_base função que cria o Base, que vamos usar nos modelos como usuario.py #git init

DATABASE_URL = "postgresql+psycopg2://USUARIO:SENHA@localhost:5432/certificados_db" # URL, precisa colocar seu usuário do pgAdmin4 e a a senha, no final o banco que criou #
                                   # COLOCA TEU USUARIO E SENHA #
engine = create_engine(DATABASE_URL) # Pega a URL e entrega, ou seja faz a ponte para o SQLAlchemy #

SessionLocal = sessionmaker(  # Cria sessão e a sessão criada conversa com o banco #
    autocommit=False, # Não confirmar o comit automaticamnete #
    autoflush=False, # Não Enviar alteração pendentes automaticamnete para o banco #
    bind=engine # permite que as sessões acessem o SQLAlchemy
)

Base = declarative_base()

