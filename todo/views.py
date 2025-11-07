from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import todoserializers
from .models import Todo





def todo_frontend(request):
    return render(request, 'todo/index.html') 


@api_view(['POST'])
def create_todo(request):
    serializer = todoserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_todo(request):
    todos = Todo.objects.all().order_by('-Created_at')
    serializer = todoserializers(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = todoserializers(todo)
    return Response(serializer.data)


@api_view(['PUT' ,"PATCH"])
def update_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = todoserializers(todo, data=request.data, partial=('PATCH' in request.method))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response({'message': 'Todo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
