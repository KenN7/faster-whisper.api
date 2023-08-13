from fastapi import FastAPI
from app.api import api_router
from app.core.config import settings
from app.core.errors import error_handler
from fastapi.middleware.cors import CORSMiddleware

from app.utils import print_routes

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)

# # Error handlers
app.add_exception_handler(422, error_handler)
app.add_exception_handler(500, error_handler)

# Print all routes
print_routes(app)
