from haber.models import Haber, HaberResim
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def index(request):
    latest_haber_list = Haber.objects.all().order_by('tarih')[:10]
    return render_to_response('haber/index.html', {'latest_haber_list': latest_haber_list})

def icerik(request, haber_id):
    try:
        h = Haber.objects.get(pk=haber_id)
    except Haber.DoesNotExist:
        raise Http404
    return render_to_response('haber/icerik.html', {'haber': h})
