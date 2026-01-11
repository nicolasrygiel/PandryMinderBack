#!/usr/bin/env python 
from fastapi import FastAPI
from routers.test import test_router

from starlette.config import Config

api_app = FastAPI()

api_app.include_router(test_router)

# TODO error management, auth