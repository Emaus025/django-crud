from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from django.contrib.auth import authenticate, login, logout  # Añade esta línea

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Username or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    username=serializer.validated_data['username'],
                    password=serializer.validated_data['password']
                )
                user.save()
                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            new_task = serializer.save(user=request.user)
            return Response(TaskSerializer(new_task).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            updated_task = serializer.save()
            return Response(TaskSerializer(updated_task).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return Response({'message': 'Task completed'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'DELETE':
        task.delete()
        return Response({'message': 'Task deleted'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signout(request):
    logout(request)
    return Response({'message': 'Logged out'})