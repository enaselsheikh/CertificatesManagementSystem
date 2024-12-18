from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class programe(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    en_Name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    full_path_name = models.CharField(max_length=100,null=False,blank=False)
    en_full_path_name = models.CharField(max_length=100,null=False,blank=False)
    desc = models.CharField(max_length=200,null=True,blank=True)
    en_desc = models.CharField(max_length=200,null=True,blank=True)
    url = models.CharField(max_length=50,null=False,blank=False)
    parent_id = models.ForeignKey('self',related_name='child_prog',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

class permession(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    desc = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name
    
class progUserPermissions(models.Model):
    user_id = models.ForeignKey(User,related_name='user_programe_permission',on_delete=models.CASCADE)
    permession_id = models.ForeignKey(permession,related_name='permession_user_program',on_delete=models.CASCADE)
    program_id = models.ForeignKey(programe,related_name='program_permission_user',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id) + '|' + str(self.permession_id) + '|' +str(self.program_id)


# class userProgram(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User,'user_id',on_delete=models.CASCADE)

# class ProgPermessions(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     permession_id = models.ForeignKey(permession,related_name='permession_id',on_delete=models.CASCADE)