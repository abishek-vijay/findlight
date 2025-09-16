from django.db import models

# Create your models here.


class Login(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'

