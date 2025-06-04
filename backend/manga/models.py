from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='manga')
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(Genre, related_name='manga')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    release_date = models.DateField()

    class Meta:
        unique_together = ('manga', 'number')
        ordering = ['number']

    def __str__(self):
        return f"{self.manga.title} — Глава {self.number}"
