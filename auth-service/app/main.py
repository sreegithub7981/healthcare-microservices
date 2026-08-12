from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from .schemas import RegisterRequest
from .database import Base, engine, get_db
from .models import User
from .schemas import LoginRequest
from .security import create_access_token

app = FastAPI(title="Auth Service")

Base.metadata.create_all(bind=engine)

password_hash = PasswordHash.recommended()


@app.get("/sree")
def root():
    return {
        "service": "auth-service",
        "status": "running"
    }


@app.post("/auth/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = password_hash.hash(request.password)

    user = User(
        email=request.email,
        password_hash=hashed_password,
        role=request.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }


@app.post("/auth/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not password_hash.verify(
        request.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "sub": str(user.id),
        "role": user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }    
