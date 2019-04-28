# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TodoSerializer
from .models import Todo


class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):

    def get_object(self, name):
        try:
            return Todo.objects.get(task_name=name)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, task_name):
        todo = self.get_object(task_name)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, task_name):
        todo = self.get_object(task_name)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, task_name):
        todo = self.get_object(task_name)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


