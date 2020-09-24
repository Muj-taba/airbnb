from django.db import models
from django.utils import timezone

# Create your models here.

Type = [
    ('Draft','Draft'),
    ('Active','Active'),
]

class Blog(models.Model):
    title       = models.CharField(max_length=30, unique=True)
    content     = models.TextField(max_length=100, null=True, blank=True)
    created_at  = models.DateTimeField(default=timezone.now)
    active      = models.BooleanField(default=True)
    auther_mail = models.EmailField(default='')
    type        = models.CharField(choices=Type, max_length=30)
    image       = models.ImageField(upload_to='media/')

