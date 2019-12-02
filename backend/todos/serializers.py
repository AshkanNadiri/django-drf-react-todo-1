from .models import Todo
from rest_framework import serializers

class Todo_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
