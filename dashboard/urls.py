from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

# from mysite.core import views


urlpatterns = [
    
    path('upload/', views.upload, name='upload'),
    path('external/', views.external,name="external"),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

