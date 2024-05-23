from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_1, name='main1'),
    path('loading/', views.main_2, name='main2'),
    path('recommend/', views.main_3, name='main3'),
]
