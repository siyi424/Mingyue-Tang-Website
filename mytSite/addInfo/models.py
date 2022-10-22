from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class PassedPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='逝者名字')
    birth = models.CharField(max_length=100, verbose_name='出生日期')
    passDate = models.CharField(max_length=100, verbose_name='逝世日期')
    gender = models.CharField(max_length=10, verbose_name='性别')
    desc = models.TextField(max_length=300, verbose_name='介绍文字')

    
