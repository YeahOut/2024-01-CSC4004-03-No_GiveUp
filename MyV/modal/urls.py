from django.urls import path, include
from . import views

urlpatterns = [
    path('analyze', views.analyzePage, name='analyze'),
    path('analyze/upload', views.upload_analyze_file, name='upload_analyze_file')
]
