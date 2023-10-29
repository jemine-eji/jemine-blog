import csv
import os


from fastapi import FastAPI, UploadFile, Form, File
from uuid import UUID
from pydantic import BaseModel
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm


app = FastAPI()

@app.get("/home")
def welcome():
    return{" Welcome To Jemine's Blog"}

@app.get("/about")
def about():
    return{" Welcome To Jemine's Blog, where you can talk about anything and advertise your goods and services completely free"}

@app.get("/login")
def login():
    return{" log into your account"}

@app.get("/signup")
def signup():
    return{" signup to Jemine's Blog"}

@app.get("/dashboard")
def dashboard():
    return{" welcome to your dashboard", "create a post"}

@app.get("/ view blog")
def view_blog():
    return {"view posts here"}

@app.get("/edit blog")
def edit_blog():
    return{" edit your post"}


