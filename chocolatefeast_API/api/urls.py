from django.urls import path
from .views import ClientView
from .views import StoreView
from .views import OrderView
from .views import PromotionView
from .views import ProductView

urlpatterns = [
    path("clients/", ClientView.as_view(), name="clients_list"),
    path("clients/<int:id>", ClientView.as_view(), name="clients_process"),
    path("stores/", StoreView.as_view(), name="stores_list"),
    path("stores/<int:id>", StoreView.as_view(), name="stores_process"),
    path("orders/", OrderView.as_view(), name="orders_list"),
    path("orders/<int:id>", OrderView.as_view(), name="orders_process"),
    path("promotions/", PromotionView.as_view(), name="promotions_list"),
    path("promotions/<int:id>", PromotionView.as_view(), name="promotions_process"),
    path("products/", ProductView.as_view(), name="products_list"),
    path("products/<int:id>", ProductView.as_view(), name="products_process"),
]
