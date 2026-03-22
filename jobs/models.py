from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('applicant', 'Applicant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
    
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, role='applicant')