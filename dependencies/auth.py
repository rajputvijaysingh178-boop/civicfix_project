from uuid import UUID

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from supabase_client import get_supabase_client

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Please log in first.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        response = get_supabase_client().auth.get_user(
            credentials.credentials
        )
    except Exception as exc:
        raise HTTPException(
            status_code=401,
            detail="Your login token is invalid or expired.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    if response.user is None:
        raise HTTPException(status_code=401, detail="User was not found.")

    user = db.get(User, UUID(str(response.user.id)))

    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="CivicFix account is inactive.")

    return user


def require_roles(*allowed_roles: str):
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="You do not have permission to do this.",
            )
        return current_user

    return role_checker