from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from label_app.views import home, search_label
from lavel_scanner import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path(r'search-label', search_label, name='search_label')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
