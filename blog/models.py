from django.db import models
from django.conf import settings
#from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)

    body = models.TextField()

    picture = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])