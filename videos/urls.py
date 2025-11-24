from django.urls import path
from .views import (
    list_videos,
    ver_video,
)

urlpatterns = [
    path('', list_videos, name='list_videos'),
    path('<int:id>/', ver_video, name="ver_video"),
]
