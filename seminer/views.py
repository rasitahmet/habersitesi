from seminer.models import Seminer
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def index(request):
    seminer_list = Seminer.objects.all().order_by('tarih')[:10]
    return render_to_response('seminer/index.html', {'seminer_list': seminer_list})

def seminer(request, seminer_id):
    try:
        s = Seminer.objects.get(pk=seminer_id)
    except Seminer.DoesNotExist:
        raise Http404
    return render_to_response('seminer/seminer.html', {'seminer': s})

# Create your views here.
