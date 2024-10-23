from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.digit_recognition import router as digit_recognition_router

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",  # allow your frontend
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the endpoints from the digit_recognition module
app.include_router(digit_recognition_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Handwritten Digit Recognition API"}
