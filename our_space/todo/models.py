from django.db import models
from authentication.models import User


class Todo(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=127, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
