from django.db import models

class UF(models.Model):
    uf_name = models.CharField(max_length=60)
    uf_initials = models.CharField(max_length=2)
