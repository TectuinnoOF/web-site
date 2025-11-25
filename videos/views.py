from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Video
from .utils import obtener_id_youtube
# Create your views here.

def list_videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos/list_videos.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Video
from .utils import obtener_id_youtube


def ver_video(request, id):
    video = get_object_or_404(Video, id=id)
    video_id = obtener_id_youtube(video.url)
    context = {
        "video": video,
        "video_id": video_id
    }
    return render(request, "videos/ver_video.html", context)
