from django.db import models
from jsonfield import JSONField


class Emails(models.Model):
    # email = models.EmailField(unique=True, null=True, blank=True)
    emails = JSONField()

    class Meta:
        verbose_name_plural = 'Email'

    # def __str__(self):
    #     return self.email.split('@')[0]