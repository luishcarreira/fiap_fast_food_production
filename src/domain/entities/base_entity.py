from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: Optional[int] = None