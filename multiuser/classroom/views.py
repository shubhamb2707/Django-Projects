from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from .models import User,Student,Teacher


def register(request):
    return render(request,'classroom/register.html')

def welcome(request):
    return render(request,'classroom/welcome.html')

def student_registration(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passagain']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'classroom/student_register.html',{'error':'User is already taken'})
            except User.DoesNotExist:
                user = User(username=request.POST['username'],
                            email=request.POST['email'],
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            is_student=True)

                user.set_password(request.POST['password'])
                user.save()
                student=Student.objects.create(user=user)
                return redirect('/classroom/login/')
        else:
            return render(request, 'classroom/student_register.html', {'error': 'Password not matched'})
    else:
        return render(request,'classroom/student_register.html')

def teacher_registration(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passagain']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'classroom/teacher_register.html',{'error':'User is already taken'})
            except User.DoesNotExist:
                user = User(username=request.POST['username'],
                            email=request.POST['email'],
                            first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            is_teacher=True,
                            is_superuser=True)

                user.set_password(request.POST['password'])
                user.save()
                teacher=Teacher.objects.create(user=user)
                return redirect('/classroom/login/')
        else:
            return render(request, 'classroom/teacher_registration.html', {'error': 'Password not matched'})
    else:
        return render(request,'classroom/teacher_registration.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user.is_student:
                login(request, user)
                return render(request,'classroom/welcome_student.html/')
            if user.is_teacher:
                login(request, user)
                return render(request,'classroom/welcome_teacher.html/')
            else:
                login(request,user)
                return render(request, 'classroom/welcome.html/')
        else:
            return render(request, 'classroom/login.html', {'form': form,
                                                  'error': 'invalid credentials'})
    else:
        form = LoginForm()
    return render(request,'classroom/login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('/classroom/login/')
