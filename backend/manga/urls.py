from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, AuthorViewSet, MangaViewSet, ChapterViewSet
from .excel_view import MangaExportExcelView
from django.shortcuts import redirect

router = DefaultRouter()
router.register('genres', GenreViewSet)
router.register('authors', AuthorViewSet)
router.register('manga', MangaViewSet)
router.register('chapters', ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('manga/export/', MangaExportExcelView.as_view(), name='manga-export-excel'),
    path('', lambda request: redirect('/api/docs/')),
]