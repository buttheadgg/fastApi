import shutil
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from ..services import min_io as init_minio
from ..import tables
from ..database import get_session

class FileOperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.infoFile]:
        fileoperation = (
            self.session
                .query(tables.infoFile)
                .all()
        )
        return fileoperation
