from pydantic import BaseModel


class BaseStudent(BaseModel):
    id: str


class ResponseInDb(BaseStudent):
    name: str
    email: str
    phone: str


class CreateStudent(BaseModel):
    name: str
    email: str
    phone: str


class UpdateStudent(BaseModel):
    name: str
    email: str
    phone: str
