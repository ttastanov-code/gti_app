from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CachedViewMixin:
    """
    Кеширование вьюхи целиком.
    Сильно снижает нагрузку и ускоряет сайт.
    """
    cache_timeout = 60 * 5  # 5 минут

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BaseListView(CachedViewMixin, ListView):
    paginate_by = 9
    context_object_name = "items"
    ordering = "-id"


class BaseDetailView(CachedViewMixin, DetailView):
    context_object_name = "item"
