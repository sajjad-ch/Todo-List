from rest_framework import viewsets
from .models import Task
from rest_framework import permissions
from .serializers import TaskSerializer
from rest_framework import generics
# Create your views here.


class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Task.objects.order_by('-priority').all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodosGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.order_by('-priority').all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
