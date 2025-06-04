import openpyxl
from django.http import HttpResponse
from .models import Manga

def export_manga_to_excel():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Manga List"

    # Заголовки
    ws.append(["ID", "Название", "Описание", "Просмотры", "Лайки", "Автор", "Дата создания"])

    for manga in Manga.objects.all():
        ws.append([
            manga.id,
            manga.title,
            manga.description,
            manga.views,
            manga.likes,
            manga.author.name if manga.author else "",
            manga.created_at.strftime('%Y-%m-%d %H:%M')
        ])

    # Сохраняем в HTTP-ответ
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=manga.xlsx'
    wb.save(response)
    return response
