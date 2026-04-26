# from datetime import datetime, timedelta
# from typing import Optional
# from passlib.context import CryptContext
# from jose import JWTError, jwt
# import sqlite3
# from .database import get_db

# # Security configuration
# SECRET_KEY = "your-secret-key-change-this-in-production"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60  # 30 days

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class AuthService:
#     @staticmethod
#     def hash_password(password: str) -> str:
#         """Hash a password"""
#         return pwd_context.hash(password)
    
#     @staticmethod
#     def verify_password(plain_password: str, hashed_password: str) -> bool:
#         """Verify a password against its hash"""
#         return pwd_context.verify(plain_password, hashed_password)
    
#     @staticmethod
#     def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
#         """Create JWT access token"""
#         to_encode = data.copy()
#         if expires_delta:
#             expire = datetime.utcnow() + expires_delta
#         else:
#             expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
#         to_encode.update({"exp": expire})
#         encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#         return encoded_jwt
    
#     @staticmethod
#     def verify_token(token: str) -> Optional[dict]:
#         """Verify JWT token"""
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#             return payload
#         except JWTError:
#             return None
    
#     @staticmethod
#     def register_user(email: str, password: str, full_name: str) -> tuple[bool, str]:
#         """Register a new user"""
#         try:
#             conn = get_db()
#             cursor = conn.cursor()
            
#             # Hash password
#             hashed_password = AuthService.hash_password(password)
            
#             # Insert user
#             cursor.execute(
#                 'INSERT INTO users (email, password, full_name) VALUES (?, ?, ?)',
#                 (email, hashed_password, full_name)
#             )
#             conn.commit()
#             conn.close()
#             return True, "User registered successfully"
#         except sqlite3.IntegrityError:
#             return False, "Email already exists"
#         except Exception as e:
#             return False, str(e)
    
#     @staticmethod
#     def login_user(email: str, password: str) -> tuple[bool, str, Optional[dict]]:
#         """Login a user"""
#         try:
#             conn = get_db()
#             cursor = conn.cursor()
            
#             # Get user
#             cursor.execute('SELECT id, email, password, full_name FROM users WHERE email = ?', (email,))
#             user = cursor.fetchone()
#             conn.close()
            
#             if not user:
#                 return False, "Email not found", None
            
#             user_id, user_email, hashed_password, full_name = user
            
#             # Verify password
#             if not AuthService.verify_password(password, hashed_password):
#                 return False, "Incorrect password", None
            
#             # Create token
#             token = AuthService.create_access_token({"sub": str(user_id), "email": user_email})
            
#             user_data = {
#                 "id": user_id,
#                 "email": user_email,
#                 "full_name": full_name,
#                 "token": token
#             }
            
#             return True, "Login successful", user_data
#         except Exception as e:
#             return False, str(e), None
    
#     @staticmethod
#     def get_user_by_email(email: str) -> Optional[dict]:
#         """Get user by email"""
#         try:
#             conn = get_db()
#             cursor = conn.cursor()
            
#             cursor.execute('SELECT id, email, full_name FROM users WHERE email = ?', (email,))
#             user = cursor.fetchone()
#             conn.close()
            
#             if user:
#                 user_id, user_email, full_name = user
#                 return {
#                     "id": user_id,
#                     "email": user_email,
#                     "full_name": full_name
#                 }
#             return None
#         except Exception as e:
#             print(f"Error getting user: {e}")
#             return None
