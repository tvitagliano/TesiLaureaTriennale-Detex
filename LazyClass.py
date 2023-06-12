import string
from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    name: str
    role: str

class Team:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Employee] = []  # Aggiunta dell'annotazione del tipo corretta

    def add_member(self, employee: Employee):
        self.members.append(employee)

    def list_members(self):
        print(f"Team: {self.name}")
        for member in self.members:
            print(f"- {member.name} ({member.role})")

# Utilizzo della classe Team
team = Team("Team A")

employee1 = Employee(name="Alice", role="Developer")
employee2 = Employee(name="Bob", role="Designer")
team.add_member(employee1)
team.add_member(employee2)

team.list_members()
