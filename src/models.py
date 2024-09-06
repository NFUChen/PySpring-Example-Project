from sqlmodel import Field
from py_spring.persistence.core.py_spring_model import PySpringModel

class Hero(PySpringModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None 