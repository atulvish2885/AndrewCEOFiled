from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . serializers import *

from rest_framework import viewsets

# Create your views here.


class SongViewSet(viewsets.ModelViewSet):

	serializer_class = SongSerializer
	queryset = Song.objects.all()

class PostcastViewSet(viewsets.ModelViewSet):

	serializer_class = PostcastSerializer
	queryset = Postcast.objects.all()
    


class AudiobookViewSet(viewsets.ModelViewSet):

	serializer_class = AudiobookSerializer
	queryset = Audiobook.objects.all()
    