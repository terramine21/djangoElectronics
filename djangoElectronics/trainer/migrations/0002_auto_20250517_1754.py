"""Миграция для добавления начальных тестовых задач в таблицу Problem."""

from django.db import migrations


def add_initial_problems(apps, schema_editor):
    """Добавляет начальные тестовые задачи в таблицу Problem, если она пуста."""
    problem_model = apps.get_model('trainer', 'Problem')
    if not problem_model.objects.exists():
        problem_model.objects.create(
            title="Закон Ома: Найти ток",
            topic="ohm",
            description="В цепи с напряжением 12 В и сопротивлением 4 Ом, найдите силу тока (I).",
            correct_answer=3.0,
            unit="А"
        )
        problem_model.objects.create(
            title="Последовательная цепь: Эквивалентное сопротивление",
            topic="series",
            description="Два резистора 6 Ом и 4 Ом соединены последовательно. "
                        "Найдите эквивалентное сопротивление.",
            correct_answer=10.0,
            unit="Ом"
        )
        problem_model.objects.create(
            title="Параллельная цепь: Эквивалентное сопротивление",
            topic="parallel",
            description="Два резистора 6 Ом и 3 Ом соединены параллельно. Найдите эквивалентное сопротивление.",
            correct_answer=2.0,
            unit="Ом"
        )
        problem_model.objects.create(
            title="Закон Кирхгофа: Найти напряжение",
            topic="kirchhoff",
            description="В цепи ток 2 А проходит через резистор 5 Ом. Найдите напряжение на резисторе.",
            correct_answer=10.0,
            unit="В"
        )


class Migration(migrations.Migration):
    """Класс миграции для добавления начальных данных в таблицу Problem."""

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_problems),
    ]
