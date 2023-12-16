# This module contains logic for password
#  hashing, for saving user password to db.

from passlib.context import CryptContext
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """
    Logic to verify user pasword upon login.

    Parameters:
        plain_password: plain text password to be verified.
        hashed_password: hashed user password from db.
    
    Return:
        success if password are same, else raises an exception.
    """

    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error -> {e}"
        )


def password_hash(password):
    """
    Password hashing function.

    Parameters:
        password: the password to be hashed.

    Return:
        the hashed password.
    """

    return pwd_context.hash(password)