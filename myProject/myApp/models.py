from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
    
class seekerProfileModel(models.Model):
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='seekerProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='recruiterProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    

class JobModel(models.Model):
    JOB_TYPE_CHOICES=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),
    ]
    user=models.ForeignKey(customUser,null=True,blank=True,on_delete=models.CASCADE)

    job_title = models.CharField(max_length=200, null=True, blank=True)  
    vacancy = models.PositiveIntegerField( null=True, blank=True) 
    skills = models. CharField(max_length=100,null=True, blank=True )
    category = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, null=True, blank=True) 
    description = models.TextField(null=True, blank=True)  
    job_Pic=models.ImageField(upload_to='Media/job_Pic',null=True)

    def __str__(self):
        return f"{self.job_title} at {self.category}"
    
class jobApplyModel(models.Model):
    user=models.ForeignKey(customUser,null=True,blank=True,on_delete=models.CASCADE)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True,blank=True)
    resume=models.FileField(upload_to='media/resume',max_length=200,null=True,blank=True)
    cover=models.TextField(null=True,blank=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    work_experience=models.CharField(max_length=100,null=True,blank=True)
    skills=models.CharField(max_length=100,null=True,blank=True)
    linkedin_url=models.URLField(max_length=100,null=True,blank=True)
    expected_salary=models.PositiveIntegerField(null=True,blank=True)
    
  