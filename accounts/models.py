from django.db import models
from teams.models import Team
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=False)
    # username = models.CharField(max_length=50, blank=False, null=False)
    # password = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    teams = models.ManyToManyField(Team, blank=True)

    #TODO: add role field
    #role = models.CharField(max_length=50, blank=True)
    team_role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.first_name