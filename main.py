from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers.books import router as book_router

app = FastAPI(title="Bookstore API")

# Include Router
app.include_router(book_router)


# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Bookstore API"
    }


# Custom 404 Handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Page not found"
        }
    )