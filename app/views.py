from fastapi import APIRouter, HTTPException
from datetime import datetime
from .models import Payload, ResponseModel
from .controllers import add_lists
from .utils import log_info, log_error

router = APIRouter()

@router.post("/add", response_model=ResponseModel)
async def add(payload: Payload):
    started_at = datetime.utcnow()
    try:
        result = add_lists(payload.payload)
        completed_at = datetime.utcnow()
        response = {
            "batchid": payload.batchid,
            "response": result,
            "status": "complete",
            "started_at": started_at,
            "completed_at": completed_at
        }
        log_info(f"Processed batch {payload.batchid} successfully")
        return response
    except Exception as e:
        log_error(f"Failed to process batch {payload.batchid}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
