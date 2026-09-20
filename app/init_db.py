from app.database.database import Base, engine # Estamos pegando do database.py o Base e o engine (engine acessa o PostgreSQL atraves da URL que fizemos) #
from app.models.usuario import Usuario # Estamos pegando do usuario.py o modelo Usuario # 

Base.metadata.create_all(bind=engine) # Aqui ele pega os modelos registrados no Base, e cria tabelas no banco que ainda não existem. ex: class Usuario(Base) e o SQLALchemy cria usuarios (__tablename__ = "usuarios") #

print("Tabelas criada com sucesso") 