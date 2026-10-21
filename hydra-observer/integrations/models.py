from django.db import models

# Create your models here.

class EnvironmentChoice(models.TextChoices):
    DEVELOPMENT = ("DEVELOPMENT", "Development")
    STAGING = ("STAGING", "Staging")
    PRODUCTION = ("PRODUCITON", "Production")

class Application(models.Model):
    """
    A Django Model to represent a observed reference appication
    """
    name = models.CharField(max_length=30)
    environment = models.CharField(
        max_length=20,
        choices=EnvironmentChoice,
        default=EnvironmentChoice.DEVELOPMENT
    )
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

