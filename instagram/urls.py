from django.contrib import admin
from django.urls import path
from myInstagram.views import *
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',singup,name="singup"),
    path("home/",home,name="home"),
    path("find-friend/",findFriend,name="findFriends"),
    path("login/",loginUser,name="login"),
    path("register/",register,name="register"),
    path("logout/",logoutUser,name="logout"),
    path("profile/",profile,name="profile"),
    path("change_profile",profile_pick,name="changeProfile"),    
    path('post/new/dp/',uploadDp,name="uploadDp"),
    path("find_friend/<int:id>/",findFri,name="findFriend"),
    path('send/<int:to_user_id>/', send_friend_request, name='send_friend_request'),
    path('accept/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('reject/<int:request_id>/', reject_friend_request, name='reject_friend_request'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
