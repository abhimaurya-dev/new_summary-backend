from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

# class SummaryBase(BaseModel):
#     headline: str
#     url: str
#     text: str

# class SummaryCreate(SummaryBase):
#     pass

class SummaryInDB(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    category: str
    summary: str
    timestamp: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
