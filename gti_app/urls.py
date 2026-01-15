from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path("admin/", admin.site.urls),

    # main
    path("", include("main.urls")),

    # content
    path("articles/", include("article.urls")),
    path("projects/", include("project.urls")),
    path("info/", include("info.urls")),
    path("request/", include("request.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
