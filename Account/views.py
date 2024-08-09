from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

@never_cache
def login_function(request):
    if request.method == "GET":
        return render(request,"Account/Login.html")

    else:
        uname = request.POST["tbusername"]
        pword = request.POST["tbpass1"]
        user = authenticate(username = uname, password = pword)

        if user != None:
            login(request,user)
            request.session['name'] = user.username
            return redirect("home")
        else:
            return redirect(("login"))

@never_cache
def register_function(request):
    if request.method == "GET":
        return render(request,"Account/Register.html")

    else:
        p1 = request.POST["tbpass1"]
        p2 = request.POST["tbpass2"]
        un = request.POST["tbusername"]
        em = request.POST["tbemail"]

        if p1 == p2:
            u = User.objects.create_superuser(un,em,p1)
            u.save()
            return redirect("login")

        else:
            return redirect("register")

@never_cache
def logout_function(request):
    del request.session['name']
    logout(request)
    return redirect("login")