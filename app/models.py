# This file will contain BaseModel classes that will define strict schemas like keywords expected inputs and outputs that the API and agent will use

# from pydantic import BaseModel, Field
# from typing import Optional
#
# class AnalyzeRequest(BaseModel):
#     text: str = Field(...,min_length=1)
#
# class AnalyzeResponse(BaseModel):
#     length: int
#     uppercase: str
#     word_count: int
#
# class HealthResponse(BaseModel):
#     status: str

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)

users_db: List[User] = []