from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class programe(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    full_path_name = models.CharField(max_length=100,null=False,blank=False)
    desc = models.CharField(max_length=200,null=True,blank=True)
    parent_id = models.ForeignKey('self',related_name='parent_id',on_delete=models.CASCADE)

class permession(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    desc = models.CharField(max_length=200,null=False,blank=False)
    
class progUserPermissions(models.Model):
    user_id = models.ForeignKey(User,'user_id',on_delete=models.CASCADE)
    permession_id = models.ForeignKey(permession,related_name='permession_id',on_delete=models.CASCADE)
    program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)


# class userProgram(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User,'user_id',on_delete=models.CASCADE)

# class ProgPermessions(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     permession_id = models.ForeignKey(permession,related_name='permession_id',on_delete=models.CASCADE)