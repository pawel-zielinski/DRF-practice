from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework import viewsets
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type = 'action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type = 'comedy')
    serializer_class = MovieSerializer
