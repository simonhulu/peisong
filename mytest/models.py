from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Cnarea(models.Model):
    id = models.IntegerField(primary_key=True, db_column="id")
    level = models.IntegerField(default=0)
    #0,未完成  1 已完成
    parent_code = models.BigIntegerField(default=0)
    area_code = models.BigIntegerField(default=0)
    zip_code = models.IntegerField(default=0)
    city_code = models.CharField(default='',max_length=250)
    name = models.CharField(default='',max_length=250)
    short_name = models.CharField(default='',max_length=250)
    merger_name = models.CharField(default='',max_length=250)
    pinyin = models.CharField(default='',max_length=250)
    lng = models.DecimalField(default=0,decimal_places=100,max_digits=10000)
    lat = models.DecimalField(default=0,decimal_places=100,max_digits=10000)
    class Meta:
        db_table = "cnarea_2018"
        managed = False