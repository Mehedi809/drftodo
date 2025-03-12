from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = '__all__'
