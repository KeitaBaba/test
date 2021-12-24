from django.db import models


class Attend(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    leavetime = models.TimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'attend'
    


