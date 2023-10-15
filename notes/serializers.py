from rest_framework import serializers
from .models import *


class NotesSerializer(serializers.ModelSerializer):
    last_edited = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S",read_only=True)
    class Meta:

        model = Notes
        fields = "__all__"