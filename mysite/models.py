# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Characters(models.Model):
    char_id = models.AutoField(db_column='char_id', primary_key=True)
    character = models.TextField()
    pinyin = models.TextField()
    tone = models.TextField() 
    translation = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)        
    class Meta:
        db_table = 'Characters'
