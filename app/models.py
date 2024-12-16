from django.db import models

# Create your models here.
class sty(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    contact=models.BigIntegerField()
    photo=models.ImageField(upload_to='images/')

class meta:
    d_table='sty'
    
