import secrets
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Token(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="auth_token")
    key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_token(user):
        key = secrets.token_hex(20)  # Generate a secure random token
        token, _ = Token.objects.update_or_create(user=user, defaults={"key": key})
        return token.key
