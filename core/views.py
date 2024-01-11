from typing import Any
from django.views.generic.base import TemplateView
from .products import Course

# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'


class ProductsListView(TemplateView):
    template_name = 'core/product_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Course.LIST_OF_COURSES
        return context
    
    # def get(self, request, *args: Any, **kwargs: Any):
    #     if 'category' not in request.GET:
    #         return super().get(request, *args, **kwargs)
        
    #     if request.GET['category'] == 'Concept':
    #         c = Course.LIST_OF_COURSES
    #         courses = [c.remove(i) for i in Course.LIST_OF_COURSES if i['category'] =='Concept']
    #     elif request.GET['category'] == 'Basic':
    #         c = Course.LIST_OF_COURSES
    #         courses = [c.remove(i) for i in Course.LIST_OF_COURSES if i['category']=='Basic']  
    #     else:
    #         courses = Course.LIST_OF_COURSES

    #     self.get_context_data(*args, **kwargs)['products'] = courses
    #     return super().get(request, *args, **kwargs)


class PythonView(TemplateView):
    template_name='core/basic_python.html'

class NetworkFundamentalView(TemplateView):
    template_name = 'core/network_fundamental.html'

class OOPView(TemplateView):
    template_name = 'core/classOOP.html'


class TextingView(TemplateView):
    template_name = 'core/texting.html'
    