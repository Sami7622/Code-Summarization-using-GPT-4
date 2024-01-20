from fastapi import FastAPI, Request, Form, Depends, HTTPException, File, UploadFile, Response, Path
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, validator
import bcrypt
import os
from database import create_connection
from users_db import users_db
import re
import pyotp
import string
from typing import List,Optional
from datetime import datetime
import shutil
from elasticsearch import Elasticsearch
import requests
# import openai fro
from openai import OpenAI

openai= OpenAI(api_key="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")
app = FastAPI()
con=create_connection()
database=con.cursor()
# CORS Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    code: str
   
# User Model
class User(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str = "User"

    @validator('password')
    def hash_password(cls, v):
        return bcrypt.hashpw(v.encode(), bcrypt.gensalt()).decode()
class LoginRequest(BaseModel):
    username: str
    password: str
    
class PaswordSet(BaseModel):
    email: EmailStr
    password: str

    @validator('password')
    def hash_password(cls, v):
        return bcrypt.hashpw(v.encode(), bcrypt.gensalt()).decode()
class Email(BaseModel):
    email: EmailStr

    




# Register Endpoint
@app.post("/register")
def register_user(user: User):
    query = "INSERT INTO users (email, passwordHash, fullName, role) VALUES (%s, %s, %s, %s)"
    values = (user.email, user.password, user.full_name, user.role)
    try:
        # Assuming database.execute() is an awaitable coroutine
        database.execute(query, values)
        con.commit()
        return {"message": "User registered successfully"}
    except Exception as e:
        return {"message":str(e)}
    

@app.post("/login")
async def login(user_data: LoginRequest):
    stored_user =  users_db().get(user_data.username)
    print(bcrypt.checkpw(user_data.password.encode('utf-8'), stored_user.password.encode('utf-8')),user_data)
    if not stored_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not(bcrypt.checkpw(user_data.password.encode('utf-8'), stored_user.password.encode('utf-8'))):
        raise HTTPException(status_code=401, detail="Unauthorized")
    print(bcrypt.checkpw(user_data.password.encode('utf-8'), stored_user.password.encode('utf-8')),user_data)
    return {"message": "Verifed sucesfully"}
    



    

@app.post("/updatePassword")
async def updatePassword(user_data:PaswordSet ):
    return  users_db().updatePassword(user_data.email,user_data.password)



@app.post("/chat")
async def chat(chat_request: ChatRequest):
    # prompt = f"Read the abstract of this thesis titled {chat_request.title}: {chat_request.abstract}. Answer the following questions from the reader. Question: {chat_request.question}"
    
    # Send the prompt to the LLM API
    try:
        response = openai.chat.completions.create(model="gpt-4", messages=[
            {"role": "system", "content":"You are a code summarize who sumarizes the entire code give to you"},
            {'role':'user','content':chat_request.code}])
        return {"response": response.choices[0]}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))