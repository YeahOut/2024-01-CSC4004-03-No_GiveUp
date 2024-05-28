from django.urls import path, include   
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', include('login.urls')),
    #path('signup/', include('signup.urls')),
    path('account/', include('allauth.urls')),
    path('team/', views.team, name='team1'),
    path('howtouse/1/', views.howtouse1, name='howtouse1'),
    path('howtouse/2/', views.howtouse2, name='howtouse2'),
    path('howtouse/3/', views.howtouse3, name='howtouse3'),
    path('howtouse/4/', views.howtouse4, name='howtouse4'),
]
