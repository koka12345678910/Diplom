from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Genre, Author, Manga, Chapter
from .serializers import GenreSerializer, AuthorSerializer, MangaSerializer, ChapterSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all().order_by('-created_at')
    serializer_class = MangaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genres', 'author']  # 🔥 Фильтрация по жанрам и автору
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'views', 'likes']
    ordering = ['-created_at']


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all().order_by('number')
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['number']
    ordering = ['number']
