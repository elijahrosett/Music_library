from rest_framework import serializers
from .models import Music

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = {"id", "artist", "album", "release_Date", "genre"}