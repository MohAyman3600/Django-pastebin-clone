from .models import Snippet
from .serializers import SnipprtSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnipprtSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnipprtSerializer


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
