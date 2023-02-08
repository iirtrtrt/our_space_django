from rest_framework import serializers
from todo.models import Todo


class TodoCreateSerializer(serializers.ModelSerializer):
    start_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])
    end_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['id', 'title', 'content', 'start_at', 'end_at']


class TodoListSerializer(serializers.ModelSerializer):
    start_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])
    end_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])

    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'title', 'content', 'start_date', 'end_date']


class TodoRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    start_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])
    end_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601'])

    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'title', 'content', 'start_at', 'end_at']
