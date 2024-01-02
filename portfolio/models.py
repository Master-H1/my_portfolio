from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_pic,resume_doc')
    resume_doc = models.FileField(upload_to='profile_pic,resume_doc',null=True,blank=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Profile Image and Resume doc'

# Job roles
class Jobroles(models.Model):
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.job

# My social media links
class Links(models.Model):
    link_name = models.CharField(max_length=100)
    link_url = models.URLField()
    link_image = models.ImageField(upload_to='links_images')

    def __str__(self):
        return self.link_name
    
    class Meta:
        verbose_name_plural = 'Links'

# Skills model 
SkillsOption ={
    ('Front-End Development','Front-End Development'),
    ('Back-End Development','Back-End Development'),
    ('OtherSkills','OtherSkills'),

}

class Skills(models.Model):
    option = models.CharField(max_length =100, choices = SkillsOption)
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Skills'

# Project model
class Projects(models.Model):
    photo = models.ImageField(upload_to='project_pic')
    title = models.CharField(max_length=100)
    technology_used = models.CharField(max_length = 100,blank=True, null=True)
    in_short = models.TextField(null=True, blank=True)
    # Description 1 of project
    title1 = models.CharField(max_length=20 ,blank=True, null=True)
    description1 = models.TextField(max_length=300, null=True, blank=True)
    photo1 = models.ImageField(upload_to='project_pic',blank=True, null=True)
    # Description 2 of project
    title2 = models.CharField(max_length=20 ,blank=True, null=True)
    description2 = models.TextField(null=True, blank=True)
    photo2 = models.ImageField(upload_to='project_pic',blank=True, null=True)
    last_update = models.DateTimeField(auto_now = True)
    # Description 3 of project
    title3 = models.CharField(max_length=20 ,blank=True, null=True)
    description3 = models.TextField(null=True, blank=True)
    photo3 = models.ImageField(upload_to='project_pic',blank=True, null=True)
    
    # Additional description
    description4 = models.CharField(max_length=100, blank=True, null=True)
    last_update = models.DateTimeField(auto_now = True)


    def __str__(self):
        return f'{self.title[:30]}...'
    
    class Meta:
        verbose_name_plural = 'Projects'