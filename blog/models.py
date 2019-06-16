from django.db import models

# Create your models here.
class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        photo = models.ImageField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def _str_(self):
                return self.title

class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.PROTECT)  #20190613 added some code by jpanda 'on_delete'
        message = models.TextField()