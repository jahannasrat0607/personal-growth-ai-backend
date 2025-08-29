from fastapi import FastAPI
from routers import auth

app = FastAPI()

# Include the auth router
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Backend is running!"}
