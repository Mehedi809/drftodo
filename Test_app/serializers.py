from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.modelserializers)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        field = all