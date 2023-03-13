from django.urls import path

from ToDoApp import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('tem',views.temp,name='temp'),
    path('tem2',views.temp2,name='temp2'),
    path('dash',views.adddata,name='adddata'),
    path('view',views.view,name='view'),
    path('ex',views.exte,name='exte'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

]