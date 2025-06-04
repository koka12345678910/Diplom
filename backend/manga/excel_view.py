from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .excel_service import export_manga_to_excel

class MangaExportExcelView(APIView):
    permission_classes = [IsAdminUser]

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return export_manga_to_excel()
