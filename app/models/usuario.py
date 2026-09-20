from sqlalchemy import Column,Integer,Index,String # importando da biblioteca sqlachemy, colunas, tipo int e string (texto) #
from app.database.database import Base  # importando da pasta app o database #

class Usuario(Base): # Criando a modelo Usuario que pertence a o banco, colocando o (Base) #
    __tablename__ = "usuarios" # O nome da tabela no PostgreSQL será "usuarios" #
    id = Column(Integer, primary_key=True, index=True) # Nome da coluna Id, Integer guarda números inteiros, primary_key=True chave primária, Index cria um índice  para a coluna. #
    nome = Column(String, nullable=False) # String é o texto e o nullable=False é obrigatório o nome #
    email = Column(String, nullable=False, index=True, unique=True) # String porque é texto, nullable=False é obrigatório, index=True cria um índice, unique=True é único. #
    senha = Column(String, nullable=False) # String é o texto e o nullable=False é obrigatório o nome #
    perfil = Column(String, nullable=False) # String é o texto e o nullable=False é obrigatório o nome #
    