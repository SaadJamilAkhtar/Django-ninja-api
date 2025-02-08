from ninja import Router
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from ninja.security import HttpBearer

from .models import Token, CustomUser

router = Router()


@router.post("/register")
def register(request, username: str, password: str):
    if CustomUser.objects.filter(username=username).exists():
        return {"error": "Username already exists"}

    user = CustomUser.objects.create_user(username=username, password=password)
    token = Token.generate_token(user)
    return {"token": token}


@router.post("/login")
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user:
        token = Token.generate_token(user)
        return {"token": token}
    return {"error": "Invalid credentials"}


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str):
        return get_object_or_404(Token, key=token).user


@router.get("/me", auth=AuthBearer())
def get_current_user(request):
    return {"username": request.auth.username}
