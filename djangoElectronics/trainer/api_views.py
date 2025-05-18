"""Модуль API-представлений для приложения trainer."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Problem, UserAnswer
from .serializers import ProblemSerializer, UserAnswerSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с задачами."""
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_permissions(self):
        """Ограничивает создание/обновление/удаление только для админов."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class UserAnswerViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с ответами пользователей."""
    serializer_class = UserAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Возвращает только ответы текущего пользователя."""
        return UserAnswer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Сохраняет ответ с текущим пользователем."""
        serializer.save(user=self.request.user)
