from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
