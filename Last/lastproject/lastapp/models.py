"""from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='student_profiles')
    student_name = models.CharField(max_length=50)
    student_username = models.CharField(max_length =10, unique = True)
    student_password  = models.CharField(max_length=10)
    student_location = models.CharField(max_length=100)
    student_qualification = models.CharField(max_length=100)
    def __str__(self):
    	return (self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		StudentProfile.objects.create(user=instance)
		print("studentprofile is craeted")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.studentprofile.save()
	print("studentprofile is saved")

class TeacherProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	subject = models.CharField(max_length=100)
	is_teacher =models.BooleanField(null=True)
	def __str__(self):
		return (self.user.username)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		TeacherProfile.objects.create(user=instance)
		print("teacherprofile is created")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.teacherprofile.save()
	print("teacherprofile is saved")
"""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser
from django.db import models

"""class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=True)
"""
class StudentProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student_profile')
	location = models.CharField(max_length=30, null=True)
	college = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		StudentProfile.objects.create(user=instance)
		print("studentprofile is craeted")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.student_profile.save()
	print("studentprofile is saved")



"""class TeacherProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='teacher_profile')
	teacher_username = models.CharField(max_length=30)
	teacher_password = models.CharField(max_length=30)
	subject = models.CharField(max_length=50)
	def __str__(self):
		return (self.user.first_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if instance.is_student:
		StudentProfile.objects.get_or_create(user = instance)
	else:
		TeacherProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	if instance.is_student:
		instance.student_profile.save()
	else:
		TeacherProfile.objects.get_or_create(user = instance)"""