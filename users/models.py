from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField(blank=False)
    website = models.URLField(max_length=200)
    bio = models.TextField(max_length=1000)
    phone_number = models.CharField(max_length=15)

    profile_picture = models.ImageField(upload_to='images/users')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    


