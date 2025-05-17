from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings


# Initialize FastAPI application with metadata from settings
app = FastAPI(
    title=settings.app_name,
    summary=settings.app_summary,
    description=settings.app_description,
    version=settings.app_version,
    debug=settings.debug,
)


# Parse allowed origins for CORS from settings
allow_origins = settings.cors_allow_origins.split(",") if settings.cors_allow_origins else ["*"]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods.split(",") if settings.cors_allow_methods else ["*"],
    allow_headers=settings.cors_allow_headers.split(",") if settings.cors_allow_headers else ["*"],
)


@app.get("/")
async def read_root():
    """
    Root endpoint returning a welcome message.
    """
    return {"message": "Welcome to FastAPI Starter Template"}
