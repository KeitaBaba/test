from django.db import models

class Users(models.Model):
    name = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

