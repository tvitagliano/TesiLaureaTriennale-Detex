import string
from typing import Optional
from pydantic import BaseModel, validator, root_validator

class SpaghettiCode(BaseModel):
    nome: str

    @validator("nome")
    @classmethod
    def nome_valid(cls, value):
       if any(p in value for p in string.punctuation):
            if len(value) < 8:
                raise ValueError("nome non presente o minore di 8 caratteri")
       else:
            return value

class Blob(BaseModel):
    metodo: str

    @validator("metodo")
    @classmethod
    def nome_valid(cls, value):
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    return value
        raise ValueError("il nome ha bisogno di una lettere maiuscola, un simbolo e un numero") 

sp = SpaghettiCode(nome="user1")
print(sp)

bb = Blob(metodo="")
print(bb)