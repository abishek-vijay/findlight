from django.db import models

# Create your models here.

class Communication(models.Model):
    co_id = models.IntegerField(primary_key=True)
    ds_id = models.IntegerField()
    response = models.CharField(max_length=200)
    u_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'communication'

