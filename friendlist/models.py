from django.db import models
from user.models import User

# Create your models here.

class Friendlist(models.Model):
    f_id = models.AutoField(primary_key=True)
    us=models.ForeignKey(User,to_field='us_id',on_delete=models.CASCADE)
    # us_id = models.IntegerField()
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'friendlist'



