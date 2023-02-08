from django.urls import path
from todo.views import TodoCreateAPI, TodoListAPI, TodoRetrieveUpdateDestroyAPI, TodoRecycleBinListAPI

urlpatterns = [
    path('list/', TodoListAPI.as_view(), name="list"),
    path('create/', TodoCreateAPI.as_view(), name="create"),
    path('updatedestroy/<int:id>',
         TodoRetrieveUpdateDestroyAPI.as_view(), name="updatedestroy"),
    path('recyclebinlist/', TodoRecycleBinListAPI.as_view(), name="recyclebinlist"),
]
