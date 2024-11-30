from pydantic import BaseModel, Field
from typing import Optional

# Address schema
class Address(BaseModel):
    city: str
    country: str

# Student schema for creation
class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

# Student schema for updates
class StudentUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]

class StudentData(BaseModel):
    name: Optional[str]
    age: Optional[int]