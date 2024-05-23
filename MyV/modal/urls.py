from django.urls import path, include
from . import views

urlpatterns = [
    #버킷 생성 및 삭제 테스트코드
    #path('analyze', views.makingbuckettest, name='analyze'),
    path('analyze', views.analyzePage, name='analyze'),
    path('analyze/upload', views.upload_analyze_file, name='upload_analyze_file'),
    path('analyze/result', views.vocalResult, name='vocalResult'),
    #path('analyze/+ing', views.vocalResult, name='vocalReport'),
]
