from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    monthly_expenses = models.IntegerField(default=0)
    goal = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.full_name
