from fastapi import FastAPI
from data_model import NewStudent,UpdateStudent

app = FastAPI(
    title = "CRUD Operations",
    description = "API for CRUD Operations"
)

Students = {
    1:{
        "name":"Shahbaz",
        "age":20
    },
    2:{
        "name":"Masab",
        "age":21
    }
}

#default case. main page. this is shown when we hit the url
@app.get("/")
def index():
    return "Welcome to the API: CRUD Operations"

#condition for http://127.0.0.1:8000/students
@app.get("/student")
def get_students():
    return Students

@app.get("/student/{stu_id}")
def get_student(stu_id: int):

    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    
    return Students[stu_id]

@app.post("/add-student")
def add_student(stu:NewStudent):
    if not Students:
        new_id = 1
    else:
        new_id = max(Students.keys()) + 1
    
    Students[new_id] = stu.model_dump()
    return Students[new_id]

@app.put("/update-student/{stu_id}")
def update_student(stu_id:int,stu:UpdateStudent):
    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    if stu.name is not None:
        Students[stu_id]["name"] = stu.name
    if stu.age is not None:
        Students[stu_id]["age"] = stu.age

    return Students[stu_id]

@app.delete("/delete-student/{stu_id}")
def delete_student(stu_id:int):
    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    
    del Students[stu_id]
    return Students