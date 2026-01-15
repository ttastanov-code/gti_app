from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta

from .models import Request
from .forms import RequestForm


class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Request
    form_class = RequestForm
    template_name = "request/form.html"
    success_url = reverse_lazy("request:form")
    success_message = "Спасибо! Ваша заявка успешно отправлена."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Обратная связь"
        return context

    def form_valid(self, form):
        # защита от флуда: максимум 1 запрос раз в 2 минуты
        time_limit = now() - timedelta(minutes=2)
        recent_count = Request.objects.filter(created_at__gte=time_limit).count()

        if recent_count > 3:
            messages.error(self.request, "Слишком много запросов. Попробуйте позже.")
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Пожалуйста, проверьте правильность заполнения формы.")
        return super().form_invalid(form)
