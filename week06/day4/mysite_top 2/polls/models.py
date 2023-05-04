from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(UserProfile,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')


    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        author = self.post.author or 'Anonymous'
        return f'{author} at {self.created_at}: {self.short_content()}'

    def short_content(self):
        return self.content[:15]