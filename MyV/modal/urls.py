from django.urls import path, include
from . import views


urlpatterns = [
    #버킷 생성 및 삭제 테스트코드
    #path('analyze', views.makingbuckettest, name='analyze'),
    path('analyze', views.analyzePage, name='analyze'),
    path('analyze/upload', views.upload_analyze_file, name='upload_analyze_file'),
    path('analyze/result', views.vocalResult, name='vocalResult'),
    path('playlist', views.playlistPage, name='playlistPage'),
    path('howtouse/1', views.howtoUse1, name='howtoUse1'),
    path('howtouse/2', views.howtoUse2, name='howtoUse2'),
    path('howtouse/3', views.howtoUse3, name='howtoUse3'),
    path('howtouse/4', views.howtoUse4, name='howtoUse4'),
    path('team', views.team, name='team'),
]
