from django.urls import path
from .views import IndexView, ProductsListView, PythonView, NetworkFundamentalView
from .views import OOPView, TextingView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  
    path('products/list', ProductsListView.as_view(), name='products-list'),
    path('introduction-to-python/', PythonView.as_view(), name='basic-python'),
    path('network-fundamental/', NetworkFundamentalView.as_view(), name='network-fundamental'),
    path('object-orientated-program/', OOPView.as_view(), name='oop'),
    path('texting/', TextingView.as_view(), name='text'),

    path('modules/', TemplateView.as_view(template_name='core/programs/pymodules.html'), name='py-modules'),
    path('introduction/', TemplateView.as_view(template_name='core/programs/pyintroduction.html'), name='py'),
    path('py-numbers/', TemplateView.as_view(template_name='core/programs/pynumbers.html'), name='py-numbers'),
    path('py-string/', TemplateView.as_view(template_name='core/programs/pystring.html'), name='py-string'),
]
