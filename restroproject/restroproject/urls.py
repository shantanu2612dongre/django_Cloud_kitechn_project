"""
URL configuration for restroproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restroapp import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('signup',views.signup_view,name='signup'),
    path('blog',views.blog_view,name='blog'),
    path('services',views.services_view,name='services'),
    path('about',views.about_view,name='about'),
    path('home',views.home_view,name='home'),
    
    path('Italian',views.Italian_view,name='Italian'),
    path('Japanese',views.Japanese_view,name='Japanese'),
    path('American',views.American_view,name='American'),
    path('Beverages',views.Beverages_view,name='Beverages'),
       
    path('oders',views.oders_view,name='oders'),
    path('recent',views.recent_view,name='recent'),
    path('order3months',views.order3months_view,name='order3months'),
    path('order6months',views.order6months_view,name='order6months'),
    path('alltime',views.alltime_view,name='alltime'),
    
    
    
    path('contactus',views.contactus_view,name='contactus'),
    path('logout',views.logout_view,name='logout'),
    path('admin/', admin.site.urls),
    
    path('profile',views.profile_view,name='profile'),
    path('userdetails',views.userdetails_view,name='userdetails'),
    path('delete/<int:id>/',views.del_view,name='delete'),
    path('menu/', views.menu, name='menu'),
    path('add_to_cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    # path('update/<int:id>/',views.update_view,name='update'),
    
    
]
