from rest_framework.serializers import ModelSerializer
from .models import Lesson
from rest_framework import serializers


def validate_video_file(file):
    max_size = 50 * 1024 * 1024
    if file.size > max_size:
        raise serializers.ValidationError("Fayl hajmi 50MB dan katta !")

    if not file.content_type in ['video/mp4', 'video/avi', 'video/mkv']:
        raise serializers.ValidationError("Fayl turi noto'g'ri. Only mp4, avi, and mkv files are allowed.")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def validate_video(self, value):
        validate_video_file(value)
        return value