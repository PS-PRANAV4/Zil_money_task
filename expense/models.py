from django.db import models

# Create your models here.

class Expenses(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name