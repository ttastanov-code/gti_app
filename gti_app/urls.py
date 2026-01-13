from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),
    path(r'jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('news/', include('article.urls')),
    # path('projects/', include('project.urls')),
    # path('info/', include('info.urls')),
    # path('request/', include('request.urls')),
]
