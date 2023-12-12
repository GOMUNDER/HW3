from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/memberdetails/<int:id>', views.memberdetails, name='memberdetails'),
    path('testing/', views.testing, name='testing'),

]
