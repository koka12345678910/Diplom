from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.shortcuts import redirect

def redirect_to_docs(request):
    return redirect('swagger-ui')

urlpatterns = [
    path('', redirect_to_docs),  # редирект с главной страницы
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    # Swagger & schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include('manga.urls')),
]
