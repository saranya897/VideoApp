from django.urls import path
from .views import RegisterUserAPIView,UserLoginAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('logout/', user_logout, name='logout'),
]