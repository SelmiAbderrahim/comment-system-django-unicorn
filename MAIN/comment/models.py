from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)
    profile_pic = models.ImageField(upload_to="authors")
    created_on = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ("-created_on", )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ("-created_on", )
