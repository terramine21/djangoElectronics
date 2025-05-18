from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problem/<int:pk>/', views.problem_detail, name='problem_detail'),
    path('result/<int:pk>/', views.result, name='result'),
    path('logout/', views.custom_logout, name='logout'),
    path('create-problem/', views.create_problem, name='create_problem'),
    path('delete-problem/<int:pk>/', views.delete_problem, name='delete_problem'),
]