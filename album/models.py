from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):

    IMAGE = '0'
    VIDEO = '1'
    STATUS_CHOICES = (
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    )
    file_type = models.CharField(max_length=1,
                                      choices=STATUS_CHOICES,
                                      default=IMAGE)
    file = models.FileField(upload_to='media_content/', blank=False)
    link = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: ".format(self.title, self.description)

    def get_absolute_url(self):
        return "/media/%i/" % self.id

    def get_edit_url(self):
        return "/media/%i/edit/" % self.id

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"
