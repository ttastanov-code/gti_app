from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.sitemaps.views import sitemap
from article.sitemaps import ArticleSitemap
from info.sitemaps import PageSitemap
from project.sitemaps import ProjectSitemap

from main.views import RobotsTxtView

sitemaps = {
    'articles': ArticleSitemap,
    'pages': PageSitemap,
    'projects': ProjectSitemap,
}

admin.site.site_header = "GTI WebApp Admin"
admin.site.site_title = "GTI WebApp Admin"
admin.site.index_title = "Панель управления"

urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path("admin/", admin.site.urls),
    
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", RobotsTxtView.as_view(), name="robots_txt"),

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
