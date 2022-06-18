from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Client
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
