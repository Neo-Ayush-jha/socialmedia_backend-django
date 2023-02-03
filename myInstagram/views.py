from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
def singup(req):
    return render(req,'singup.html')

@login_required()
def home(req):
    data={}
    # {'user':User.objects.filter(username=req.user).values().first()}
    data['post']=User.objects.all()
    data['account']=Account.objects.exclude(user=req.user)
    data['new_post']=Post.objects.order_by("-id")
    return render(req,"index.html",data)



def send_friend_request(request, to_user_id):
    to_user = User.objects.get(id=to_user_id)
    FriendRequest.objects.create(from_user=request.user, to_user=to_user)
    return redirect(home)

def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    friend_request.status = True
    friend_request.save()
    return redirect('friend_list')

def reject_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    friend_request.delete()
    return redirect('friend_list')


@login_required()
def profile(req):
    data={}
    data['user']=User.objects.filter(username=req.user).values().first()
    data['acc']=Account.objects.exclude(user=req.user)
    data['new_post']=Post.objects.all()
    sent_friend_requests = FriendRequest.objects.filter(from_user=req.user)
    received_friend_requests = FriendRequest.objects.filter(to_user=req.user)
    data['request_count']=FriendRequest.objects.count()
    
    friend_requests_sent = FriendRequest.objects.filter(to_user=req.user).count()
    data = {'friend_requests_sent': friend_requests_sent}

    # data['to']=FriendRequest.objects.filter('sent_friend_requests': sent_friend_requests,'received_friend_requests': received_friend_requests,)  
    data={'sent_friend_requests': sent_friend_requests,'received_friend_requests': received_friend_requests}

    
    return render(req,"profile.html",data)

@login_required()
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

def findFri(req,id):
    data={}
    data['far']=Account.objects.get(pk=id)
    return render(req,home,data)

