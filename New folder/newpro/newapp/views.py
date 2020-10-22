from django.shortcuts import render
from .models import StudentProfile, TeacherProfile,User
from .forms import StudentProfileForm, TeacherProfileForm, UserForm
from django.http import HttpResponse


def student_profile_view(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = StudentProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()

			user.StudentProfile.location = profile_form.cleaned_data['location']
			user.StudentProfile.save()
		else:
			return HttpResponse("Invalid User Data")	
	else:
		user_form = UserForm()
		profile_form = StudentProfileForm()
		return render(request, 'student_profile.html',{
			'user_form': user_form,
			'profile_form': profile_form,
		})


def teacher_profile_view(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = TeacherProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()

			user.TeacherProfile.subject = profile_form.cleaned_data.get('subject')
			user.TeacherProfile.save()
		else:
			return HttpResponse("Invalid User Data")	
	else:
		user_form = UserForm(prefix='UF')
		profile_form = TeacherProfileForm()
		return render(request, 'teacher_profile.html',{
			'user_form': user_form,
			'profile_form': profile_form,
		})



