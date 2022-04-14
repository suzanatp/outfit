from outfit.web.models import Outfit
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = Outfit
    template_name = 'web/dashboard.html'
    context_object_name = 'outfit_photos'
