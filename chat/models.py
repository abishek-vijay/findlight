from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    us_id = models.IntegerField()
    message = models.CharField(max_length=30)
    sendertype = models.CharField(max_length=30)
    rectype = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat'






