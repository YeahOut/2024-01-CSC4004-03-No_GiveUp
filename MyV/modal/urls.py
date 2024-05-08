from django.urls import path, include
from . import views

urlpatterns = [
    path('analyze', views.analyze, name='analyze'),
]
