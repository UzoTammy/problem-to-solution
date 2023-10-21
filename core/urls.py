from django.urls import path
from .views import IndexView, ProductsListView, PythonView, NetworkFundamentalView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  
    path('products/list', ProductsListView.as_view(), name='products-list'),
    path('introduction-to-python/', PythonView.as_view(), name='introduction-to-python'),
    path('network-fundamental/', NetworkFundamentalView.as_view(), name='network-fundamental')
]
