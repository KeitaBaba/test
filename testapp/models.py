from django.db import models

class Users(models.Model):
    name = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Attend(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    in_out = models.CharField(max_length=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attend'
    


