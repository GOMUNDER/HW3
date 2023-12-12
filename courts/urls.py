from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('courts/', views.courts, name='courts'),
    path('courts/courtdetails/<int:id>', views.courtdetails, name='courtdetails'),

]
