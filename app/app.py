from __future__ import annotations

from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.config.base import settings
from app.middlewares.request_id_injection import RequestIdInjection
from app.routes import api_router
from app.utils.exception_handler import (exception_handler,
                                         http_exception_handler,
                                         validation_exception_handler)

# Check required environment variables
settings.check_environment_variables()

app = FastAPI(
    title="FastAPI Template",
    description="This is my first API use FastAPI",
    version="0.0.1",
    openapi_tags=[{"name": "FastAPI Template", "description": "API template using FastAPI."}],
    docs_url="/",
)
origins = settings.ALLOWED_HOSTS

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestIdInjection)

# Include the routers
app.include_router(api_router, prefix="/api")

# Exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, exception_handler)

# Add pagination support
add_pagination(app)
