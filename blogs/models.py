from django.db import models
from user.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title
