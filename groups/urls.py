from django.urls import path 
from . import views


urlpatterns=[
    path('',views.dashboard, name='dashboard'),
    path('create/', views.create_group,name='create_group'),

]