from galeri.models import Album, Resim
from django.contrib import admin

class ResimInline(admin.StackedInline):
    model = Resim
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ResimInline]

admin.site.register(Album, AlbumAdmin)

#from galeri.models import Album
#from django.contrib import admin

#admin.site.register(Album)
