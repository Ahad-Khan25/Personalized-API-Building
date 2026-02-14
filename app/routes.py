# This file connects HTTP world, validation layer and business logic layer

# from fastapi import APIRouter
# from .models import AnalyzeRequest, AnalyzeResponse, HealthResponse
# from .services import analyze_text
#
# router = APIRouter(prefix="/api/v1")
#
# @router.get("/health",response_model=HealthResponse)
# def health():
#     return {"status":"running"}
#
# @router.post("/analyze",response_model=AnalyzeResponse)
# def analyze(request: AnalyzeRequest):
#     result = analyze_text(request.text) #analyze_text is the function (business logic defined in services.py) which takes the text according to the format defined in AnalyzeRequest base model
#     return result

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from fastapi import APIRouter, HTTPException
from typing import Optional, List
from .models import User, users_db

router = APIRouter(prefix="/api/v2")

# Get all Users
@router.get("/users",response_model=List[User])
def get_users():
    return users_db

# Get single user by id
@router.get("/user/{user_id}",response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Post add a new user
@router.post("/new",response_model=User,status_code=201)
def new_user(user: User):
    for u in users_db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    users_db.append(user)
    return user

# Patch update a user partially
@router.patch("/update/{user_id}",response_model=User)
def update_user(user_id: int, updated: dict):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            updated_user_data = user.dict()
            updated_user_data.update(updated)
            users_db[idx] = User(**updated_user_data)
            return users_db[idx]
    raise HTTPException(status_code=404, detail="User not found")

# Delete a User
@router.delete("/delete/{user_id}",status_code=204)
def delete_user(user_id: int):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="User not found")