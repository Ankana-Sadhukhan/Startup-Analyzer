from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .predictor import predict_idea
# from .auth_routes import router as auth_router

app = FastAPI()


# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include auth routes
# app.include_router(auth_router, prefix="/auth", tags=["auth"])

@app.get("/")
def home():
    return {"message": "Startup Idea Analyzer API 🚀"}

@app.get("/predict")
def predict(idea: str):
    return predict_idea(idea)