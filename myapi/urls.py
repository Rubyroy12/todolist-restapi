from django.urls import path,include
from . import views



urlpatterns = [
    path(r'^api/merch/$', views.HeroList.as_view()),
    path('',views.home, name ='home')
]
