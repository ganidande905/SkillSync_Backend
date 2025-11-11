from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash:
    @staticmethod
    def hash(password: str) -> str:
        """Hash a password using argon2."""
        return pwd_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """Verify a plain password against its hash."""
        return pwd_context.verify(plain_password, hashed_password)