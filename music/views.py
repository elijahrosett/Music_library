from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from .serializers import MusicSerializer



@api_view(['GET', 'POST'])
def music_list(request):
    music = Music.objects.all()
    serializer = MusicSerializer(music, many=True)


    return Response(serializer.data)