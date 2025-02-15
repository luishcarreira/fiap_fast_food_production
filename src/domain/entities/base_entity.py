from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: Optional[int] = None
    u_inserted: int
    inserted: datetime
    u_updated: Optional[int] = None
    updated: Optional[datetime] = None