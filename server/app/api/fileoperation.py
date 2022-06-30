import aiofiles
from fastapi import (
    APIRouter,
    FastAPI,
    UploadFile,
    File,
    status
)
from datetime import datetime
from fastapi import Depends
from typing import List
from fastapi.responses import JSONResponse
import uuid
from ..models.auth import User
from ..models.fileoperation import fileoperation
from ..services.auth import get_current_user
from ..services.fileoperations import FileOperationService
from .import min_io as mm
from app import database as db

router = APIRouter(
    prefix='/FileOperations',
    tags=['FileOperations']
)

@router.post('/frames',response_model=List[fileoperation])
async def create_upload_file(
        files:List[UploadFile] = File(...),
        user: User = Depends(get_current_user)
):
    now = datetime.now()
    code = now.strftime("%Y%m%d%H%M%S")
    try:
        for file in files:
            new_filename = str(uuid.uuid4()) + '.jpg'
            db.add_new_data_to_database(code, file.filename)
            mm.add_new_data_to_minio(code, new_filename, file)

        db.session.commit()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'message': str(e)}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"result": code}
        )

@router.get("/frames/{code}")
async def get_data(
        code: str,
        user: User = Depends(get_current_user)
):
    results = db.search_data_by_code_request(code)
    return {code: [{result.name_saved_file: result.registration_date} for result in results]}

@router.delete("/frames/{code}")
async def delete_data(
        code: str,
        user: User = Depends(get_current_user)
):
    db.delete_data_by_code_request(code)
    mm.delete_data_by_code_request(code)
    content = {
        code: True
    }
    return JSONResponse(content=content)



