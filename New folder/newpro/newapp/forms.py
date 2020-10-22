from django import forms 
from .models import StudentProfile,TeacherProfile,User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('location',)
        
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ("subject",)


        