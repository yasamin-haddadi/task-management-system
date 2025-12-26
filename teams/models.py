from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Team(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_ARCHIVED = 'archived'
    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
        (STATUS_ARCHIVED, 'Archived'),
    ]

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/',
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])
            ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
