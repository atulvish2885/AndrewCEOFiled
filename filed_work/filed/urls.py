from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url


from .views import SongViewSet, PostcastViewSet, AudiobookViewSet

router = routers.DefaultRouter()
router.register('songs',SongViewSet)
router.register('postcast',PostcastViewSet)
router.register('audiobook',AudiobookViewSet)




urlpatterns=[
	path('fileapi_filed/',include(router.urls)),
]