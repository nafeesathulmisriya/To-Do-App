from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)  # ✅ CREATED DATE
    due_date = models.DateTimeField(null=True, blank=True)

    category = models.CharField(max_length=100, default="General")

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Completed", "Completed")
        ],
        default="Pending"
    )

    def __str__(self):
        return self.title
