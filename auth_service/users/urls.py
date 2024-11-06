from django.urls import path
from .views import UserCreateView, MyTokenObtainPairView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]