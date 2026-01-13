from django.conf import settings

def analytics(request):
    return {
        "YANDEX_METRIKA_ID": settings.YANDEX_METRIKA_ID,
        "GOOGLE_ANALYTICS_ID": settings.GOOGLE_ANALYTICS_ID,
        "debug": settings.DEBUG,
    }
