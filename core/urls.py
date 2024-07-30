from django.contrib import admin
from django.urls import path, include
from projects import urls
from users import urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# production settings
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)