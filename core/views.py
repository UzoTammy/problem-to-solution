from typing import Any
from django.views.generic.base import TemplateView
from .models import Course

# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'


class ProductsListView(TemplateView):
    template_name = 'core/product_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(pk=1)
        return context

    

class PythonView(TemplateView):
    template_name='core/basic_python.html'

class NetworkFundamentalView(TemplateView):
    template_name = 'core/network_fundamental.html'

class OOPView(TemplateView):
    template_name = 'core/classOOP.html'


class TextingView(TemplateView):
    template_name = 'core/texting.html'
    