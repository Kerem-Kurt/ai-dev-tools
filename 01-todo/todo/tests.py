from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Todo
from datetime import timedelta

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title="Test Todo", description="Test Description")
        self.assertTrue(isinstance(todo, Todo))
        self.assertEqual(todo.__str__(), todo.title)
        self.assertFalse(todo.completed)

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(
            title="Test Todo", 
            description="Test Description",
            created_date=timezone.now()
        )

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo_create'), {
            'title': 'New Todo',
            'description': 'New Description',
            'due_date': ''
        })
        self.assertEqual(response.status_code, 302) # Redirect after success
        self.assertEqual(Todo.objects.count(), 2)

    def test_todo_update_view(self):
        response = self.client.post(reverse('todo_update', args=[self.todo.pk]), {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'completed': 'on',
            'due_date': ''
        })
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertTrue(self.todo.completed)

    def test_todo_delete_view(self):
        response = self.client.post(reverse('todo_delete', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)
