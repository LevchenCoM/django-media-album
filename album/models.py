from django.db import models
from django.contrib.auth.models import User
class Media(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    file = models.FileField(upload_to='media_content/', blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: ".format(self.title, self.description)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"
