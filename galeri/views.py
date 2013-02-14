from galeri.models import Album, Resim
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def index(request):
    latest_album_list = Album.objects.all().order_by('tarih')[:12]
    return render_to_response('galeri/index.html', {'latest_album_list': latest_album_list})

def album(request, album_id):
    try:
        resimler_list = Album.objects.get(pk=album_id).resimler.all().order_by('tarih')
        #a = Album.objects.get(pk=album_id)
        #resimler_list = a.resimler.all().order_by('tarih')
    except Album.DoesNotExist:
        raise Http404
    return render_to_response('galeri/album.html', {'resimler_list': resimler_list})

# Create your views here.
