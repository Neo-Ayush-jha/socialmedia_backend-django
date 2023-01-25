from django.contrib import admin
from django.urls import path
from myInstagram.views import *
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',singup,name="singup"),
    path("home/",home,name="home"),
    path("login/",loginUser,name="login"),
    path("register/",register,name="register"),
    path("logout/",logoutUser,name="logout"),
    path("profile/",profile,name="profile")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)