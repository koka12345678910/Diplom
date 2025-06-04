from rest_framework import serializers
from .models import Genre, Author, Manga, Chapter

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'manga', 'number']

class MangaSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Manga
        fields = [
            'id', 'title', 'description', 'cover', 'author',
            'genres', 'views', 'likes', 'created_at', 'chapters'
        ]
