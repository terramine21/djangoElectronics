# Тренажер по электрическим цепям

## Описание

Тренажер по электрическим цепям — это образовательный веб-сервис, разработанный на Python с использованием фреймворка Django и Django Rest Framework. Пользователи могут решать задачи с автоматической проверкой ответов через веб-интерфейс или API, а суперпользователи — управлять задачами.

Сервис использует SQLite для хранения данных, Tailwind CSS для стилизации интерфейса и реализует валидацию ввода.

## Функционал

- **Веб-интерфейс**:
  - Просмотр каталога задач, разделенных по темам.
  - Решение задач с вводом ответа и автоматической проверкой.
  - Просмотр результатов ответа.
  - Аутентификация через страницу логина.
  - Создание и удаление задач суперпользователем.

- **API (Django Rest Framework)**:
  - Эндпоинты: `/api/problems/` и `/api/user-answers/`.
  - Просмотр, создание, обновление, удаление задач (админы).
  - Создание и просмотр ответов (аутентифицированные пользователи).
  - Аутентификация через Django-сессии.

- **Технические особенности**:
  - Адаптивный интерфейс с Tailwind CSS.
  - Хранение данных в SQLite.
  - Ограничение доступа через декораторы и DRF-permissions.

## Требования

- Python 3.8+
- Django 5.2.1
- Django Rest Framework 3.15.2

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/terramine21/djangoElectronics.git
   cd djangoElectronics/djangoElectronics
   ```

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Примените миграции**:
   ```bash
   python manage.py migrate
   ```

4. **Создайте суперпользователя**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```

6. Откройте: `http://127.0.0.1:8000/`

## Использование

- **Веб-интерфейс**:
  - Главная: `/`
  - Каталог задач: `/problems/`
  - Задача: `/problem/<id>/`
  - Результат: `/result/<id>/`
  - Создание задачи: `/create-problem/` (админ)
  - Удаление задачи: `/delete-problem/<id>/` (админ)
  - Админ-панель: `/admin/`
  - Логин/логаут: `/accounts/login/`, `/logout/`

- **API**:
  - `GET /api/problems/`: Список задач.
  - `POST /api/problems/`: Создать задачу (админ).
  - `GET/PUT/DELETE /api/problems/<id>/`: Детали/обновление/удаление задачи (админ).
  - `GET /api/user-answers/`: Список ответов текущего пользователя.
  - `POST /api/user-answers/`: Создать ответ.
  - Аутентификация: Используйте Django-сессии (логин через `/admin/`).

## Разработка

- **Фреймворк**: Django 5.2.1, Django Rest Framework 3.15.2
- **База данных**: SQLite
- **Стилизация**: Tailwind CSS (CDN)
- **Валидация**: Django forms и DRF serializers
- **Ограничение доступа**: Django декораторы и DRF permissions
