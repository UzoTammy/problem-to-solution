from django.urls import path
from .views import IndexView, ProductsListView, PythonView, NetworkFundamentalView
from .views import OOPView, TextingView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  
    path('products/list', ProductsListView.as_view(), name='products-list'),
    path('introduction-to-python/', PythonView.as_view(), name='basic-python'),
    path('network-fundamental/', NetworkFundamentalView.as_view(), name='network-fundamental'),
    path('object-orientated-program/', OOPView.as_view(), name='oop'),
    path('texting/', TextingView.as_view(), name='text')
]
