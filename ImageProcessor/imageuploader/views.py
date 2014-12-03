from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from imageuploader.models import *
from imageuploader.serializers import PhotoSerializer
from django.http.response import Http404
from rest_framework import status
from django.http.multipartparser import FILE

class PhotoList(APIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        photo = MyPhoto.objects.all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(data=serializer.data, status = status.HTTP_200_OK)
    """
    def post(self, request, format=FILE):
       serializer = PhotoSerializer(data=request.DATA)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   """ 
    def post(self, request, *args, **kwargs):
        try:
            image = request.FILES['image']
            # Image processing here.
            return Response(status=status.HTTP_201_CREATED)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail' : 'Expected image.'})

    def pre_save(self, obj):
        obj.owner = self.request.user


class PhotoDetail(APIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return MyPhoto.objects.get(pk=pk)
        except MyPhoto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def pre_save(self, obj):
        obj.owner = self.request.user
