"""Миграция для создания начальных моделей Problem и UserAnswer."""

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    """Класс миграции для создания таблиц Problem и UserAnswer."""

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('title', models.CharField(max_length=200)),
                ('topic', models.CharField(
                    choices=[
                        ('ohm', 'Закон Ома'),
                        ('series', 'Последовательные цепи'),
                        ('parallel', 'Параллельные цепи'),
                        ('kirchhoff', 'Законы Кирхгофа')
                    ],
                    max_length=20
                )),
                ('description', models.TextField()),
                ('correct_answer', models.FloatField()),
                ('unit', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('answer', models.FloatField()),
                ('is_correct', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='trainer.problem'
                )),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
    ]
