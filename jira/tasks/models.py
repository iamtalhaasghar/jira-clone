from django.db import models


class User(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=256, default=None)
    start_date = models.DateTimeField('start date')
    is_complete = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'Name:{}, Complete:{}, Assigned To:{}'.format(self.name, self.is_complete, self.assigned_to)
