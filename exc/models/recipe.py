#!/usr/bin/env python
from datetime import datetime, timezone
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Index, Integer, DateTime, String
from sqlalchemy.types import JSON
from typing import Optional

from models.base_model import BaseModel

class RecipeTable(BaseModel):
    __tablename__ = 'pdm_recipe'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime(tzinfo=timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime(tzinfo=timezone.utc), 
        onupdate=datetime(tzinfo=timezone.utc)
    )