
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from todo.serializers import TodoCreateSerializer, TodoListSerializer, TodoRetrieveUpdateDestroySerializer
from todo.models import Todo
from rest_framework import permissions
from .permissions import IsUser


class TodoCreateAPI(CreateAPIView):
    serializer_class = TodoCreateSerializer
    queryset = Todo.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TodoListAPI(ListAPIView):
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all().order_by('-id')
    permission_classes = (permissions.IsAuthenticated, IsUser,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, is_deleted=False)


class TodoRecycleBinListAPI(ListAPIView):
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all().order_by('-id')
    permission_classes = (permissions.IsAuthenticated, IsUser,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, is_deleted=True)


class TodoRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoRetrieveUpdateDestroySerializer
    permission_classes = (permissions.IsAuthenticated, IsUser,)
    queryset = Todo.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
