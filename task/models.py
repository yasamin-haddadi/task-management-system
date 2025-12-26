from django.db import models
from accounts.models import Account
from teams.models import Team

class Task(models.Model):
    IMPORTANCE_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    label = models.CharField(max_length=50, blank=True, null=True)
    importance = models.CharField(max_length=15, choices=IMPORTANCE_CHOICES, default='medium')
    user = models.ManyToManyField(Account,
                                  related_name='tasks',
                                  blank=True)
    team = models.ForeignKey(Team,
                                on_delete=models.CASCADE,
                                related_name='tasks',blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)







    def __str__(self):
        return self.name    
