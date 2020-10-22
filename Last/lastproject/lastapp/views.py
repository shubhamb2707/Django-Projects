'''from django.http import HttpResponse
from django.shortcuts import render 
from .models import StudentProfile,TeacherProfile, User
from .forms import StudentProfileForm,TeacherProfileForm, UserForm'''
"""from django.http import HttpResponse
from django.shortcuts import render 
from .models import StudentProfile, User
from .forms import StudentProfileForm, UserForm
def student_profile_view(request):
    if request.method == "POST":
        sform = StudentProfileForm(request.POST,prefix='SF')
        uform = UserForm(request.POST,prefix='UF')
        if  sform.is_valid() and uform.is_valid():
            user = uform.save(commit=False)
            user.save()
            user.student_profile.student_username = sform.cleaned_data.get("student_username")
            user.student_profile.student_password = sform.cleaned_data.get("student_password")
            user.student_profile.location = sform.cleaned_data.get("location")
            user.student_profile.save()
            return HttpResponse("succefully Student user created")
        else:
            return HttpResponse("Invalid User Input")
    else:
        uform = UserForm(prefix='UF')
        sform = StudentProfileForm(prefix='SF')
        return render(request, "studentform.html", {"uform":uform,"sform":sform})
"""
'''def teacher_profile_view(request):
    if request.method == "POST":
        uform = UserForm(request.POST,prefix='UF')
        tform = TeacherProfileForm(request.POST,prefix='TF')
        if  uform.is_valid() and tform.is_valid():
            user = uform.save(commit=False)
            user.save()
            user.teacher_profile.teacher_username = tform.cleaned_data.get("teacher_username")
            user.teacher_profile.teacher_password = tform.cleaned_data.get("teacher_password")
            user.teacher_profile.subject = tform.cleaned_data.get("subject")
            user.teacher_profile.save()
            return HttpResponse("succefully teacher user created")
        else:
            return HttpResponse("InvalidUserInput")

    else:
        uform = UserForm(prefix='UF')
        tform = TeacherProfileForm(prefix='TF')
        return render(request, "teacherform.html", {"uform":uform, "tform":tform})
"""
from .forms import InternProfileForm,UserForm
from django.shortcuts import render
from django.http import HttpResponse
def intern_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = InternProfileForm(request.POST, prefix='PF')    
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            user.intern_profile.bio = profile_form.cleaned_data.get('bio')
            user.intern_profile.location = profile_form.cleaned_data.get('location')
            user.intern_profile.save()
            return HttpResponse("Form Submitted")
        else:
            return HttpResponse("invalid")
    else:
        user_form = UserForm(prefix='UF')
        profile_form = InternProfileForm(prefix='PF')
        return render(request, 'studentform.html',{
            'user_form': user_form,
            'profile_form': profile_form,
        })

"""

'''
from .models import StudentProfile,User
from .forms import StudentProfileForm
from django.shortcuts import render
def Student_Profile_View(request):
    if request.method=="POST":
        form=StudentProfileForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            location=form.cleaned_data.get('location')
            college=form.cleaned_data.get('college')

            pqr = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                )
            user_instance = pqr.save()

            xyz=StudentProfile(
                user_instance=user,
                location=location,
                college= college,
            )
            xyz.save()


            form=StudentProfileForm()
            return render(request,'studentform.html',{'form':form})
        else:
            form=StudentProfileForm()
            return HttpResponse("Invalid User Input data")
    else:
        
        form=StudentProfileForm()
        return render(request,'studentform.html',{'form':form})

