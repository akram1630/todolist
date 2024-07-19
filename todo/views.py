from django.shortcuts import redirect, render , get_object_or_404 

from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['myTitle']
        )
        new_todo.save()
        return redirect('/')  
                                        #or context={'todos':todo}            
    return render(request,'index.html',{'todos':todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/') # to refresh
############################################################################
@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True) #to convert to json | qs== query Set
    return Response({"todoList":serializer.data })

@api_view(['GET'])
def todoById(request,myPk):
    todos = get_object_or_404(Todo,id=myPk)
    serializer = TodoSerializer(todos,many=False) #to convert to json | qs== query Set
    return Response({"todoById":serializer.data })

#######################################################################
@api_view(['POST'])
def newTask(request):
    data = request.data
    serializer = TodoSerializer(data=data) #to convert to json

    if serializer.is_valid(): #form is filled
        task = serializer.validated_data.get('title')
        task = Todo(
            title = task
        )
        task.save()
        res = TodoSerializer(task , many=False) #many = we created one task
        return Response({"task":res.data})
    else:
        Response(serializer.errors)
################################################################################
@api_view(['DELETE'])
def deleteApi(request, pkD):
    try:
        task = Todo.objects.get(id=pkD)
        task.delete()
        return Response({"task": "deletion has been successful"}, status=status.HTTP_204_NO_CONTENT)
    except Todo.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)