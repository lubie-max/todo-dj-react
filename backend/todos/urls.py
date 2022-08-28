from django.urls import path 
from .views import *
urlpatterns = [
    path('', home , name="home" ),
    path('api/<int:pk>/', TaskAPIView.as_view() ),
    path('api/', TaskAPIView.as_view()  ),
]