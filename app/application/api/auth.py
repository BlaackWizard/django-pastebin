from ninja import Router
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

auth_router = Router()


@auth_router.post("/register")
def register(request, username: str, password: str):
    if User.objects.filter(username=username).exists():
        return {"error": "User already exists"}

    user = User.objects.create(
        username=username,
        password=make_password(password)  # Хэшируем пароль
    )
    token, _ = Token.objects.get_or_create(user=user)
    return {"token": token.key}


@auth_router.post("/login")
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user is None:
        return {"error": "Invalid credentials"}

    token, _ = Token.objects.get_or_create(user=user)
    return {"token": token.key}
