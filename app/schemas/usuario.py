from pydantic import BaseModel # Importando a classe BaseModel do pydantic #

class  UsuarioCreate(BaseModel): # Criando um schema chamado UsuarioCreate
    nome: str
    email: str
    senha: str
    perfil: str