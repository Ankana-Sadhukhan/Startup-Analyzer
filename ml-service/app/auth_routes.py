# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from .auth_service import AuthService
# from .database import get_db
# import sqlite3

# router = APIRouter()

# class SignUpRequest(BaseModel):
#     email: str
#     password: str
#     full_name: str

# class LoginRequest(BaseModel):
#     email: str
#     password: str

# class AuthResponse(BaseModel):
#     success: bool
#     message: str
#     data: dict = None

# @router.post("/signup")
# async def signup(request: SignUpRequest):
#     """Register a new user"""
#     # Validate input
#     if not request.email or not request.password or not request.full_name:
#         raise HTTPException(status_code=400, detail="Missing required fields")
    
#     if len(request.password) < 6:
#         raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    
#     # Register user
#     success, message = AuthService.register_user(
#         request.email,
#         request.password,
#         request.full_name
#     )
    
#     if not success:
#         raise HTTPException(status_code=400, detail=message)
    
#     # Create token for new user (auto-login)
#     token = AuthService.create_access_token({"sub": request.email, "email": request.email})
    
#     return {
#         "success": True,
#         "message": "Signup successful!",
#         "data": {
#             "email": request.email,
#             "full_name": request.full_name,
#             "token": token,
#             "is_new": True
#         }
#     }

# @router.post("/login")
# async def login(request: LoginRequest):
#     """Login a user"""
#     # Validate input
#     if not request.email or not request.password:
#         raise HTTPException(status_code=400, detail="Email and password are required")
    
#     # Login user
#     success, message, user_data = AuthService.login_user(request.email, request.password)
    
#     if not success:
#         raise HTTPException(status_code=401, detail=message)
    
#     return {
#         "success": True,
#         "message": message,
#         "data": {
#             **user_data,
#             "is_new": False
#         }
#     }

# @router.get("/verify-token/{token}")
# async def verify_token(token: str):
#     """Verify JWT token"""
#     payload = AuthService.verify_token(token)
    
#     if not payload:
#         raise HTTPException(status_code=401, detail="Invalid token")
    
#     # Get user info
#     email = payload.get("email")
#     user = AuthService.get_user_by_email(email)
    
#     if not user:
#         raise HTTPException(status_code=401, detail="User not found")
    
#     return {
#         "success": True,
#         "data": user
#     }
