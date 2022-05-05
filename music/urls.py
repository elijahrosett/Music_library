from django.urls import path 
from . import views


urlpatterns = [
    path('api/music/', views.music_list),
    path('api/music/<int:pk>/', views.music_detail)
]