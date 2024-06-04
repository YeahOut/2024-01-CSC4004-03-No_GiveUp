from django.urls import path
from . import views
urlpatterns = [
    path('css/',views.css),
    path('', views.main_1, name='main1'),
    path('upload/', views.upload_max_min, name='upload_max_min'),
    path('loading/', views.main_2, name='loading'),
    path('recommend/', views.main_3, name='main3'),
    path('test/', views.test, name='test'),
]
