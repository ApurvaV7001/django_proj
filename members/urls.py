from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    
    #path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),

]

