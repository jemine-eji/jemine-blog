import csv
import os

from fastapi import FastAPI, file, UploadFile, Form, Depends, HTTPException, status
from typing import list, Optional, Annotated
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
 
from csvs import user, create_user

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "JP246"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = CryptContext(schemes=["bcrypt"], depreciated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_csv_file = "new.csv"

blog_posts = []
next_user_id =1
next_blog_post_id = 1

@app.post("/register", response_model=user)
def create_user(user: create_user):
    user_id = len(user_id) + 1
    hashed_password = password_hash.hash(user.password)
    print(hashed_password)


def load_user_from_csv():
    users = []
    if os.path.exists(user_csv_file):
        with open(user_csv_file, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                users.append(user(**row))
    return users

#function to save user data to csv file
def save_users_to_csv(users):
    with open(user_csv_file, mode="w", newline="") as csv_file:
        fieldnames = ["id", "first_name", "last_name", "email", "password"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for user in users:
            csv_writer.writerow(user.dict())


# use database (in memory list, replace with a database in a real app)
class Blogpost(BaseModel):
    title: str
    content: str

#blog post model
class BlogPostmodel(Blogpost):
    id: int
    author_id: int

#Blog posts database (in-memory list)
blog_posts = load_user_from_csv()

#Endpiont to register a new user
@app.post("/register", response_model=user)
def create_user(user: create_user):
    user_id = len(user_id) + 1
    hashed_password = password_hash.hash(user.password)

# Function to verify password
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

# Endpoint to lidt all blog posts
@app.get("/blogposts", response_model=list[BlogPostmodel])
def list_blog_posts():
    return blog_posts

# Endpoint to view blog post by ID
@app.get("/blog-posts/{blog_post_id}", response_model=BlogPostmodel)
def view_blog_post(blog_post_id):
    post = next((post for post in blog_posts if post.id == blog_post_id), None)
    if post is None:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return post
