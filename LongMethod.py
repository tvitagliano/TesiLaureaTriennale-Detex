import string
from typing import Optional
from pydantic import BaseModel, validator, root_validator


class UserData(BaseModel):
    name: str
    age: int
    email: str

class UserProcessor:
    def process_user_data(self, user_data: UserData):
        self.validate_user_data(user_data)
        self.perform_data_operations(user_data)

    def validate_user_data(self, user_data: UserData):
        # Validazione dei dati dell'utente
        if user_data.age < 18:
            raise ValueError("L'età dell'utente deve essere maggiore di 18 anni.")
        # Altre validazioni...
    
    def perform_data_operations(self, user_data: UserData):
        # Operazioni sui dati dell'utente
        self.update_user_profile(user_data)
        self.send_email_notification(user_data)

    def update_user_profile(self, user_data: UserData):
        # Aggiornamento del profilo dell'utente
        pass
    
    def send_email_notification(self, user_data: UserData):
        # Invio di una notifica via email all'utente
        pass

# Utilizzo della classe UserProcessor
user_data = UserData(name="Alice", age=25, email="alice@example.com")
processor = UserProcessor()
processor.process_user_data(user_data)

#
