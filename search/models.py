# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Cnword(models.Model):
    # 词,解释,全拼
    words = models.CharField(max_length=255, blank=True)
    explain = models.TextField()
    py = models.CharField(max_length=255)

    class Meta:
        db_table = 'cnword'

    def __unicode__(self):
        return self.words
