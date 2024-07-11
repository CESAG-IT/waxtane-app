
from django.contrib import admin
from django.urls import include, path

from core.views import home_view, about_view, contact_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/', include('tags.urls')),
    path('topics/', include('topics.urls')),
    path('', home_view, name="home"),
    path('about', about_view, name="about"),
    path('contact', contact_view, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
