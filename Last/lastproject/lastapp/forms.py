'''from .models import StudentProfile,TeacherProfile,User
from django.contrib.auth.models import User

from django import forms 


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('student_username','student_password','location')


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ('teacher_username','teacher_password','subject')

"""
from .models import User, InternProfile, HRProfile
from django import forms 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class InternProfileForm(forms.ModelForm):
    class Meta:
        model = InternProfile
        fields = ('location', 'bio')
        
class HRProfileForm(forms.ModelForm):
    class Meta:
        model = HRProfile
        fields = ('company_name', 'website')
"""
'''


from django import forms
class StudentProfileForm(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First_Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    last_name=forms.CharField(
        label="Enter Your Last_Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )



    username=forms.CharField(
        label="Enter Your username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username'
            }
        )
    )
    
    password=forms.CharField(
        label="Enter Your passowrd",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
            }
        )
    )

    student_location=forms.CharField(
        label="Enter Your location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your location'
            }
        )
    )

    college=forms.CharField(
        label="Enter Your college",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your college'
            }
        )
    )

