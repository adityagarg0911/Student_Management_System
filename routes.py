from fastapi import APIRouter, HTTPException, Path, Query
from models import StudentCreate, StudentUpdate, StudentData
from database import students_collection
from bson import ObjectId

router = APIRouter(prefix="/students", tags=["Students"])

# Helper to format response
def format_student_data(student):
    return {
        "name": student["name"],
        "age": student["age"],
    }

def format_student_id(student):
    return {
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }

# Create a new student
@router.post("/", status_code=201)
async def create_student(student: StudentCreate):
    result = await students_collection.insert_one(student.dict())
    return {"id": str(result.inserted_id)}

# List students with optional filters
@router.get("/")
async def list_students(country: str = Query(None), age: int = Query(None)):
    filters = {}
    # if country:
    #     filters["address.country"] = country
    # if age:
    #     filters["age"] = {"$gte": age}
    filters["address.country"] = country
    filters["age"] = {"$gte": age}
    
    students = await students_collection.find(filters).to_list(100)
    return {"data": [format_student_data(s) for s in students]}

# Fetch a student by ID
@router.get("/{id}")
async def get_student(id: str = Path(...)):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return format_student_id(student)

# Update a student
@router.patch("/{id}", status_code=201)
async def update_student(id: str, student: StudentUpdate):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    result = await students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}

# Delete a student
@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}
