"""Модуль маршрутов URL для приложения trainer."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import ProblemViewSet, UserAnswerViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'user-answers', UserAnswerViewSet, basename='user-answer')

urlpatterns = [
    path('', views.home, name='home'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problem/<int:pk>/', views.problem_detail, name='problem_detail'),
    path('result/<int:pk>/', views.result, name='result'),
    path('logout/', views.custom_logout, name='logout'),
    path('create-problem/', views.create_problem, name='create_problem'),
    path('delete-problem/<int:pk>/', views.delete_problem, name='delete_problem'),
    path('api/', include(router.urls)),  # API маршруты
]
