from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
def singup(req):
    return render(req,'singup.html')

@login_required(redirect_field_name="login")
def home(req):
    data={}
    data['account']=Account.objects.all()
    # {'user':User.objects.filter(username=req.user).values().first()}
    data['post']=User.objects.all()
    data['new_post']=Post.objects.all()
    return render(req,"index.html",data)

@login_required(redirect_field_name="login")
def profile(req):
    return render(req,"profile.html",{'user':User.objects.filter(username=req.user).values().first(),'acc':Account.objects.filter(user=req.user),'new_post':Post.objects.all()})

@login_required(redirect_field_name="login")
def profile_pick(req):
    if req.method == "POST":
        P=Post()
        P.post_by=User.objects.get(username=req.user)
        P.image=req.FILES.get('image')
        P.caption=req.POST.get("caption")
        P.save()
        return redirect(home)
        
       

def loginUser(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        
        # user = authenticate(username=username, password=password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(req,user)
            return redirect("home")
        else:
            return render(req,"login.html")
    return render(req,"login.html")

def register(req):
    if req.method == "POST":
        S=User()
        S.first_name = req.POST.get("fname")
        S.last_name=req.POST.get("lname")
        S.email = req.POST.get("email")
        S.set_password(req.POST.get('password'))
        S.username = req.POST.get("username")
        S.is_active = True
        S.is_staff = True
        S.save()
        

        A=Account()
        A.user = S
        A.contact= req.POST.get("contact")
        A.image=req.FILES.get("image")
        A.gender = req.POST.get('gender')
        A.dob = req.POST.get("dob")
        A.save()
        
        return redirect(singup)
def logoutUser(req):
    logout(req)
    return redirect(loginUser)

