#!/usr/bin/env python
from datetime import datetime

from fastapi import APIRouter, Depends

from entities.test import TestEntity

# -- Create router --
test_router = APIRouter(
  prefix='/tests',

  tags=["tests"]
)

# --- ROUTES ---
@test_router.get('')
async def get_tests():
    test_list = TestEntity.get_test_list()
    return {"test_list": test_list} 

@test_router.get('{test_id}')
async def get_test(test_id: int):
    return {}
