from django.views import generic as views

from outfit.web.models import Outfit


class SunnyWeatherView(views.ListView):
    model = Outfit
    template_name = 'web/weather/sunny-weather.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.filter(weather='Sunny')
        context['user'] = self.request.user
        return context


class WindyWeatherView(views.ListView):
    model = Outfit
    template_name = 'web/weather/windy-weather.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.filter(weather='Windy')
        return context


class RainyWeatherView(views.ListView):
    model = Outfit
    template_name = 'web/weather/rainy-weather.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.filter(weather='Rainy')
        context['user'] = self.request.user
        return context


class SnowWeatherView(views.ListView):
    model = Outfit
    template_name = 'web/weather/snow-weather.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.filter(weather='Snow')
        context['user'] = self.request.user
        return context


class OtherWeatherView(views.ListView):
    model = Outfit
    template_name = 'web/weather/other-weather.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.filter(weather='N/A')
        context['user'] = self.request.user
        return context
