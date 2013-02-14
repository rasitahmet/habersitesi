from yazarlar.models import Yazar, Yazi
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def index(request):
    yazar_list = Yazar.objects.all()
    return render_to_response('yazarlar/index.html', {'yazar_list': yazar_list})

def yazar(request, yazar_id):
    try:
        yazilar_list = Yazar.objects.get(pk=yazar_id).yazilar.all().order_by('tarih')
    except Yazar.DoesNotExist:
        raise Http404
    return render_to_response('yazarlar/yazar.html', {'yazilar_list': yazilar_list})

def yazi(request, yazi_id):
    try:
        y = Yazi.objects.get(pk=yazi_id)
    except Yazi.DoesNotExist:
        raise Http404
    return render_to_response('yazarlar/yazi.html', {'yazi': y})
# Create your views here.
