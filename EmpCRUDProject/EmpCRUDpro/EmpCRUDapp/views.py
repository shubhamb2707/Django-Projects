from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import EmployeeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout, authenticate
@login_required(login_url="/login")
def CreateView(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/index")
        else:
            return HttpResponse("Invalid Data Entered")
    else:
        form = EmployeeForm()
        return render(request, "create_view.html", {"form":form})

@login_required(login_url="/login")
def IndexView(request):
    data = EmployeeData.objects.all()
    return render(request, "Retrieve.html", {"data":data})



def DeleteView(request, fname):
    ddata = EmployeeData.objects.get(fname=fname)
    ddata.delete()
    return redirect("/index")





def UpdateView(request, fname):
    udata=EmployeeData.objects.get(fname=fname)
    if request.method == "POST":
        form=EmployeeForm(request.POST, instance=udata)
        if form.is_valid():
            form.save()
        return redirect("/index")
    return render(request, "updateform.html", {"udata":udata})



def Loginview(request):
    if request.method == "POST":
        Username1 = request.POST.get('uname')
        Password2 = request.POST.get('psw')
        from django.contrib.auth import authenticate, login
        user = authenticate(username=Username1, password=Password2)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            else:
                return redirect("/index/")
        else:
            return HttpResponse("<h3>Invalid User Name ANd Password</h3>")

    else:
        return render(request, "login.html")