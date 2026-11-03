
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.config.settings import APP_NAME, APP_VERSION
from app.routers.product_routes import router as product_router


# Configure application logging.
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
#Logging – recording application activities and errors.
#Exception handling – controlling what response the API sends when an error occurs.

# Create FastAPI application.
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="ShopEase Product Management REST API",
)


# Register Product API routes.
app.include_router(product_router)


# Handle invalid request data.
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "detail": "Request validation failed",
            "errors": exc.errors(),
        }),
    )


# Handle unexpected application errors.
@app.exception_handler(Exception)
async def unexpected_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unexpected error: %s %s",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
        },
    )


# Home endpoint.
@app.get("/")
def home():
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
    }


# Health endpoint.
@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
