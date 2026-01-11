#!/usr/bin/env python
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, Index, Integer, String
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import JSON

from models.base_model import BaseModel

class IngredientTable(BaseModel):
    __tablename__ = 'pdm_ingredient'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    type: Mapped[int] = mapped_column(Integer) 
    status: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime(tzinfo=timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime(tzinfo=timezone.utc), 
        onupdate=datetime(tzinfo=timezone.utc)
    )

class IngredientTypeTable(BaseModel):
    __tablename__ = 'pdm_ingredient_type'
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


    
class IngredientStock(BaseModel):
    __tablename__ = 'pdm_ingredient_stock'
    id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(Integer) # TODO externak key
    amount: Mapped[int] = mapped_column(Integer) 
    amount_type: Mapped[int] = mapped_column(Integer) # TODO enum
    in_date: Mapped[datetime] = mapped_column(DateTime)
    peremption_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime(tzinfo=timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime(tzinfo=timezone.utc), 
        onupdate=datetime(tzinfo=timezone.utc)
    )
    
class IngredientPrice(BaseModel):
    __tablename__ = 'pdm_ingredient_price'
    id: Mapped[int] = mapped_column(primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(Integer) # TODO externak key
    price: Mapped[int] = mapped_column(Integer) 
    currency: Mapped[int] = mapped_column(Integer) # TODO enum
    date: Mapped[int] = mapped_column(Integer) # TODO enum
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime(tzinfo=timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime(tzinfo=timezone.utc), 
        onupdate=datetime(tzinfo=timezone.utc)
    )
    
