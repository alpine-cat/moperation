from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from .serializers import AdvSerializer, UserSerializer
from .models import Adv
from django.contrib.auth.models import User


class AdvViewSet(viewsets.ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = [filters.SearchFilter]
    search_fields = ['wn8', 'wins_percent']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
