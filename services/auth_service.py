from uuid import UUID

from sqlalchemy.orm import Session

from models.user import User
from schemas.auth import UserCreate, UserLogin, Token
from schemas.common import Message
from supabase_client import get_supabase_client


class AuthServiceError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def register_user(data: UserCreate, db: Session) -> Message:
    supabase = get_supabase_client()

    try:
        response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password,
            }
        )
    except Exception as exc:
        raise AuthServiceError(
            "Registration failed. Check the email and password.",
            400,
        ) from exc

    if response.user is None:
        raise AuthServiceError("Supabase did not create the account.", 400)

    profile = User(
        id=UUID(str(response.user.id)),
        name=data.name,
        email=data.email,
        role="resident",
        department_id=None,
    )

    try:
        db.add(profile)
        db.commit()
    except Exception as exc:
        db.rollback()
        raise AuthServiceError(
            "The account was created, but its profile could not be saved.",
            500,
        ) from exc

    return Message(
        message="Account created. Check your email if confirmation is required."
    )


def login_user(data: UserLogin) -> Token:
    supabase = get_supabase_client()

    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": data.email,
                "password": data.password,
            }
        )
    except Exception as exc:
        raise AuthServiceError(
            "Email or password is incorrect.",
            401,
        ) from exc

    if response.session is None:
        raise AuthServiceError(
            "No login session was returned. Confirm your email, then try again.",
            401,
        )

    return Token(
        access_token=response.session.access_token,
        refresh_token=response.session.refresh_token,
        token_type="bearer",
    )