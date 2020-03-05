from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cnarea
import json
from django.forms.models import model_to_dict
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

def index(request):
    page = int(request.GET.get('page',0))
    size = int(request.GET.get('size', 20))
    start = page *size
    arr = list(Cnarea.objects.all()[start:start+size])
    has_next = True
    if len(arr) < size:
        has_next = False
    dics = []
    for obj in arr:
        dic = model_to_dict(obj)
        dics.append(dic)
    dic = {"list":dics,"page":page,"hasNext":has_next}
    return HttpResponse(json.dumps(dic,cls=DecimalEncoder), content_type='application/json')