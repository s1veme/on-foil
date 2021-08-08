from django.views.generic import TemplateView

from gallery.models import Gallery


class LandingView(TemplateView):
    template_name = 'lending/index.html'

    def get_context_data(self, **kwargs): 
        context = kwargs 
        context['gallery'] = Gallery.objects.all()
        return context