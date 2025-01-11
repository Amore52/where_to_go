from django.contrib import admin
from django.urls import path, include
from where_to_go_config import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('place/<int:place_id>/', views.place_details, name='place_details'),
    path('tinymce/', include('tinymce.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
