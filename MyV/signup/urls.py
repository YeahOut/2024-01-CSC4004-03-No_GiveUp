from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.signup1, name='signup1'),
    path('2/', views.signup2, name='signup2'),
    path('3/', views.signup3, name='signup3'),
    path('3/upload', views.upload_view, name='upload_view'),
    path('done/', views.done, name='done'),
    path('account/signup/', views.CustomSignupView.as_view(), name='account_signup'),
]
