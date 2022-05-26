from django.db import models


class Site(models.Model):
    MODE_CHOICES = [
        ('a', 'A'),
        ('b', 'B'),
    ]
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='a')
    name = models.CharField(max_length=100)
    value = models.IntegerField(primary_key=True, blank=False, unique=True)

    class Meta:
        ordering = ['value']
        db_table = 'site'