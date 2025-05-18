"""Конфигурация приложения trainer."""

from django.apps import AppConfig


class TrainerConfig(AppConfig):
    """Конфигурация приложения trainer для Django."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trainer'