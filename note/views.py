from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Note,Notice
from .serialaizers import NoteSerializers,NoticeSerializers


class NoteVieset(GenericViewSet,UpdateModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin):
    serializer_class = NoteSerializers
    queryset = Note.objects.all()


class NoticeVieset(GenericViewSet,UpdateModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin):

    serializer_class = NoticeSerializers
    queryset = Notice.objects.all()

