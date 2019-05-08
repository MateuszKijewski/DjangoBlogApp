from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField()
    content = models.TextField(max_length = 5000)
    date_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
