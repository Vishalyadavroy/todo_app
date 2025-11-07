from rest_framework import serializers
from .models import Todo

class todoserializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = Todo

    title = serializers.CharField(required=True)
    completed = serializers.BooleanField(required=True)
