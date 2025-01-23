from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from app.models import User
from app.schemas import UserCreate, Token, LoginRequest
from app.utils.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

# Registro de usuario
@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, username=user.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User registered successfully"}

# Inicio de sesion
@router.post("/login", response_model=Token)
def login(request: LoginRequest, db:Session = Depends(get_db)):
    username = request.username
    password = request.password
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = f"fake-token-for-{username}"
    return {"acces_token": token, "token_type": "Bearer"}