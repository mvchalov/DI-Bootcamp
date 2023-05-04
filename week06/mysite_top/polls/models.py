from django.db import models
from accounts.models import UserProfile
from django.core.validators import MinLengthValidator, MaxValueValidator
from .validators import date_validator
from django.core.exceptions import ValidationError
from datetime import date
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    author = models.ForeignKey(UserProfile,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    
    date_created = models.DateField(null=True, validators=[date_validator])
    slug = models.SlugField(unique=True, max_length=60, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def clean(self) -> None:
        super().clean()
        if self.title.lower().endswith('z') and self.date_created == date.today():
            raise ValidationError("Title mustn't end with 'z' and the date shouldnt be today's date ")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.post.title} | {self.created_at} | {self.short_content()}"
    
    def short_content(self):
        return self.content[:15]
