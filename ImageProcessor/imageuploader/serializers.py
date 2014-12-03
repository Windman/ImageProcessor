from imageuploader.models import MyPhoto
from rest_framework import serializers
from django.core.context_processors import request
 
class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyPhoto
        fields = ('url', 'id', 'image', 'owner')
        owner = serializers.Field(source='owner.username')


