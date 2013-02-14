from roportaj.models import Roportaj
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def index(request):
    roportaj_list = Roportaj.objects.all().order_by('tarih')[:10]
    return render_to_response('roportaj/index.html', {'roportaj_list': roportaj_list})

def roportaj(request, roportaj_id):
    try:
        r = Roportaj.objects.get(pk=roportaj_id)
    except Roportaj.DoesNotExist:
        raise Http404
    return render_to_response('roportaj/roportaj.html', {'roportaj': r})
# Create your views here.
