from django.test import TestCase
from core.models import User, Task
from datetime import date

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="João Silva", email="joao@email.com")

    def test_create_user(self):
        self.assertEqual(self.user.name, "João Silva")
        self.assertEqual(self.user.email, "joao@email.com")

    def test_update_user(self):
        self.user.name = "Maria Souza"
        self.user.save()
        self.assertEqual(self.user.name, "Maria Souza")

    def test_delete_user(self):
        user_id = self.user.id
        self.user.delete()
        self.assertFalse(User.objects.filter(id=user_id).exists())


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Carlos Silva", email="carlos@email.com")
        self.task = Task.objects.create(
            title="Fazer compras",
            description="Comprar leite e pão",
            status="pending",
            due_data=date.today(),
            user=self.user
        )

    def test_create_task(self):
        self.assertEqual(self.task.title, "Fazer compras")
        self.assertEqual(self.task.description, "Comprar leite e pão")
        self.assertEqual(self.task.status, "pending")
        self.assertEqual(self.task.user.name, "Carlos Silva")

    def test_update_task_status(self):
        self.task.status = "completed"
        self.task.save()
        self.assertEqual(self.task.status, "completed")

    def test_delete_task(self):
        task_id = self.task.id
        self.task.delete()
        self.assertFalse(Task.objects.filter(id=task_id).exists())
