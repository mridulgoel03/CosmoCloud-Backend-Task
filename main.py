from fastapi import FastAPI, HTTPException
from models import students_collection
from schemas import Student, UpdateStudent
from bson import ObjectId

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management System"}

def serialize_student(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "class": student["class"],
        "email": student.get("email")
    }

@app.post("/students", status_code=201)
async def create_student(student: Student):
    student_data = student.dict(by_alias=True)
    result = await students_collection.insert_one(student_data)
    new_student = await students_collection.find_one({"_id": result.inserted_id})
    return serialize_student(new_student)

@app.get("/students/{student_id}")
async def get_student(student_id: str):
    student = await students_collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return serialize_student(student)

@app.get("/students")
async def list_students():
    students = await students_collection.find().to_list(100)
    return [serialize_student(student) for student in students]

@app.put("/students/{student_id}")
async def update_student(student_id: str, updates: UpdateStudent):
    update_data = {k: v for k, v in updates.dict(by_alias=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No updates provided")
    result = await students_collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
    if not result.matched_count:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student = await students_collection.find_one({"_id": ObjectId(student_id)})
    return serialize_student(updated_student)

@app.delete("/students/{student_id}", status_code=204)
async def delete_student(student_id: str):
    result = await students_collection.delete_one({"_id": ObjectId(student_id)})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return None
