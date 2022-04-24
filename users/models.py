from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bio(models.Model):
    website = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField()
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.bio[:15]