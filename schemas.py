from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: int
    class_: str = Field(..., alias="class")
    email: Optional[str] = None

    class Config:
        allow_population_by_field_name = True  # Allows alias for 'class'

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    class_: Optional[str] = Field(None, alias="class")
    email: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
