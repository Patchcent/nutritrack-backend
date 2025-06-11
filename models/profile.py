from pydantic import BaseModel

class UserProfile(BaseModel):
    email: str
    edad: int = 0
    peso: float = 0.0
    altura: float = 0.0
    objetivos: str = ""