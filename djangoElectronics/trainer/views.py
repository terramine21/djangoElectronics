"""Модуль представлений для приложения trainer."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Problem, UserAnswer
from .forms import AnswerForm, ProblemForm


def home(request):
    """Отображает главную страницу."""
    return render(request, 'trainer/home.html')


def problem_list(request):
    """Отображает список всех задач."""
    problems = Problem.objects.all()
    return render(request, 'trainer/problem_list.html', {'problems': problems})


@login_required
def problem_detail(request, pk):
    """Обрабатывает страницу задачи и ввод ответа."""
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            is_correct = abs(answer - problem.correct_answer) < 0.01
            UserAnswer.objects.create(
                user=request.user,
                problem=problem,
                answer=answer,
                is_correct=is_correct
            )
            return redirect('result', pk=pk)
    else:
        form = AnswerForm()
    return render(
        request,
        'trainer/problem_detail.html',
        {'problem': problem, 'form': form}
    )


@login_required
def result(request, pk):
    """Отображает результат ответа пользователя."""
    problem = get_object_or_404(Problem, pk=pk)
    user_answer = UserAnswer.objects.filter(
        user=request.user, problem=problem
    ).latest('submitted_at')
    return render(
        request,
        'trainer/result.html',
        {'problem': problem, 'user_answer': user_answer}
    )


def custom_logout(request):
    """Обрабатывает выход пользователя из системы."""
    logout(request)
    return redirect('home')


@user_passes_test(lambda u: u.is_superuser)
def create_problem(request):
    """Обрабатывает создание новой задачи суперпользователем."""
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно создана!')
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'trainer/create_problem.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def delete_problem(request, pk):
    """Обрабатывает удаление задачи суперпользователем."""
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == 'POST':
        problem.delete()
        messages.success(request, 'Задача успешно удалена!')
        return redirect('problem_list')
    return render(
        request,
        'trainer/delete_problem_confirm.html',
        {'problem': problem}
    )