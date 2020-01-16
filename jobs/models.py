from django.db import models

# Create your models here.
class JobItem(models.Model):
    uuid = models.UUIDField(default=None, blank=True)
    status = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField()
    search_word = models.CharField(max_length=100)
    result = models.CharField(max_length=10, default='-')

    class Meta:
        ordering = ('created',)
