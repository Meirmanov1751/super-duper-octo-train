from rest_framework import serializers


from .models import Note,Notice


class NoteSerializers(serializers.ModelSerializer):

    class Meta:
        model=Note
        fields=['id','note','created_date','updated_date']


class NoticeSerializers(serializers.ModelSerializer):

    class Meta:
        model=Notice
        fields=['id','title','note','note_created_date','created_date','updated_date']


