from pydantic import BaseModel
from typing import List
from datetime import datetime

class Payload(BaseModel):
    batchid: str
    payload: List[List[int]]

class ResponseModel(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
