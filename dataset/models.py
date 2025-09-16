from django.db import models

# Create your models here.

class DataSet(models.Model):
    ds_id = models.IntegerField(db_column='DS_id')  # Field name made lowercase.
    type = models.CharField(max_length=100)
    emotions = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'data_set'


