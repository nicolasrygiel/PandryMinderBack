#!/usr/bin/env python
from datetime import datetime, timezone
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Index, Integer, DateTime, String
from sqlalchemy.types import JSON
from typing import Optional

from models.base_model import BaseModel

class TestTable(BaseModel):
    __tablename__ = 'pdm_test'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_str: Mapped[str] = mapped_column(String(64), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    