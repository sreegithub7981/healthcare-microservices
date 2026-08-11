import jwt
from datetime import datetime, timedelta, timezone
SECRET_KEY = "super-secret-key-change-this-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload["exp"] = expire
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )