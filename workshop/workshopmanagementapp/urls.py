from django.urls import path

from workshopmanagementapp import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('tem', views.temp, name='temp'),
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('log', views.log, name='log'),
    path('login_view', views.log, name='login_view'),
    path('worker_register', views.worker_register, name='worker_register'),
    path('reg', views.reg, name='reg'),


]