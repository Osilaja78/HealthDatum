# This module contains logic for generating
# user token.

from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt
import os


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict, expires_delta: timedelta):
    """
    Generates access token for authenticated users.

    Parameters:
        data: dictionary of user data.
        expires_delta: time for token expiration.

    Return:
        encoded_jwt: encoded jwt token generated.
    """

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
