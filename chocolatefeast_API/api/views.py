from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Client
from .models import Store
from .models import Order
from .models import Promotion
from .models import Product
import json

# Create your views here.
class ClientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            clients = list(Client.objects.filter(id=id).values())
            if len(clients) > 0:
                client = clients[0]
                data = {"message": "Success", "client": client}
            else:
                data = {"message": "Clients not found..."}
            return JsonResponse(data)
        else:
            clients = list(Client.objects.values())
            if len(clients) > 0:
                data = {"message": "Success", "clients": clients}
            else:
                data = {"message": "Clients not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        c = Client.objects.create(name=jd["name"], budget=jd["budget"])
        data = {"message": "Sucess", "id": c.id}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        clients = list(Client.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Client.objects.get(id=id)
            client.name = jd["name"]
            client.budget = jd["budget"]
            client.save()
            data = {"message": "Sucess"}
        else:
            data = {"message": "Client not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        jd = json.loads(request.body)
        clients = list(Client.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Client.objects.get(id=id)
            client.delete()
            data = {"message": "Sucess"}
        else:
            data = {"message": "Client not found"}
        return JsonResponse(data)


class StoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            stores = list(Store.objects.filter(id=id).values())
            if len(stores) > 0:
                store = stores[0]
                data = {"message": "Success", "client": store}
            else:
                data = {"message": "Store not found..."}
            return JsonResponse(data)
        else:
            stores = list(Store.objects.values())
            if len(stores) > 0:
                data = {"message": "Success", "stores": stores}
            else:
                data = {"message": "Store not found..."}
            return JsonResponse(data)


class OrderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            orders = list(Order.objects.filter(id=id).values())
            if len(orders) > 0:
                order = orders[0]

                # Traer cliente
                orderQuery = Order.objects.get(id=id)
                orderClient = orderQuery.client
                orderProducts = list(orderQuery.products.all())
                orderProductsPromotions = list(orderProducts[0].promotions.all())

                def chocolateFeast(n, c, m):
                    choco = n // c
                    wraps = choco

                    while wraps >= m:
                        choco += wraps // m
                        wraps = wraps // m + wraps % m

                    return choco

                result = chocolateFeast(
                    orderClient.budget,
                    orderProducts[0].price,
                    orderProductsPromotions[0].wraps,
                )

                data = {
                    "message": "Success",
                    "order": order,
                    "chocolatefeast": result,
                    "clientName": orderClient.name,
                }
            else:
                data = {"message": "order not found..."}
            return JsonResponse(data)
        else:
            orders = list(Order.objects.values())
            if len(orders) > 0:
                data = {"message": "Success", "orders": orders}
            else:
                data = {"message": "order not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        c = Order.objects.create(
            quantity=jd["quantity"],
            client=jd["client"],
            store=jd["store"],
            products=jd["products"],
        )
        data = {"message": "Sucess", "id": c.id}
        return JsonResponse(data)


class PromotionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            promotions = list(Promotion.objects.filter(id=id).values())
            if len(promotions) > 0:
                promotion = promotions[0]
                data = {"message": "Success", "Promotion": promotion}
            else:
                data = {"message": "promotion not found..."}
            return JsonResponse(data)
        else:
            promotions = list(Promotion.objects.values())
            if len(promotions) > 0:
                data = {"message": "Success", "Promotions": promotions}
            else:
                data = {"message": "promotion not found..."}
            return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        promotions = list(Promotion.objects.filter(id=id).values())
        if len(promotions) > 0:
            promotion = Promotion.objects.get(id=id)
            promotion.wraps = jd["wraps"]
            promotion.save()
            data = {"message": "Sucess"}
        else:
            data = {"message": "Promotion not found..."}
        return JsonResponse(data)


class ProductView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            products = list(Product.objects.filter(id=id).values())
            if len(products) > 0:
                product = products[0]
                data = {"message": "Success", "product": product}
            else:
                data = {"message": "product not found..."}
            return JsonResponse(data)
        else:
            products = list(Product.objects.values())
            if len(products) > 0:
                data = {"message": "Success", "products": products}
            else:
                data = {"message": "product not found..."}
            return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            product = Product.objects.get(id=id)
            product.name = jd["name"]
            product.price = jd["price"]
            product.save()
            data = {"message": "Sucess"}
        else:
            data = {"message": "Product not found..."}
        return JsonResponse(data)
