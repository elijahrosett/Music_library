from rest_framework.decorators import api_view
from rest_framework.response import Response

from music.models import Music


@api_view(['GET', 'POST'])
def music_list(request):
    music = Music.objects.all()


    return Response("ok")