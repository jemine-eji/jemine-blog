import csv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


@app.post("/user")
async def create_user(user: user):
    with open("new.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.id, user.first_name, user.last_name, user.email])
    return{"message": "User created successfully", "data": user}

@app.get("/user{id}")
async def get_user(id: int):
    with open ("new.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if int(row[0]) == id:
                return user(id=int(row[0]), first_name=(row[1]),last_name=(row[2]), email=(row[3]))
    return{"message": "user is not fount"}
    
@app.put("/user/{id}")
async def update_user(id: int, user: user):
    rows = []
    with open('new.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if int(row[0]) == id:
                rows.append([user.id, user.first_name, user.last_name, user.email])
            else:
                rows.append(row)

