from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static 



urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('add_post/', views.add_post,name="add_post"),

    
    # Auth
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),


    path('<str:slug>/',views.single,name="single"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 