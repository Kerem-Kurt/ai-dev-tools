# Django Todo App

A simple Todo application built with Django for the AI Dev Tools course (HW1).

## Features
- Create, Read, Update, Delete (CRUD) Todos
- Due dates and completion status
- Admin interface integration
- Full test coverage

## Quick Start

1. **Install Dependencies**
   ```bash
   # Create/activate venv
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install Django
   pip install django
   ```

2. **Run Migrations**
   ```bash
   cd 01-todo
   python manage.py migrate
   ```

3. **Run Tests**
   ```bash
   python manage.py test
   ```

4. **Start Server**
   ```bash
   python manage.py runserver
   ```
   Visit: http://127.0.0.1:8000/
