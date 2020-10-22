from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(AbstractUser):
    is_student = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=30, blank=True)

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_student:
        StudentProfile.objects.get_or_create(user = instance)
    else:
        TeacherProfile.objects.get_or_create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('_-----')
    if instance.is_student:
        instance.student_profile.save()
    else:
        TeacherProfile.objects.get_or_create(user = instance)