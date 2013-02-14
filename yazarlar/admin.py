from yazarlar.models import Yazar, Yazi
from django.contrib import admin

#class ResimInline(admin.StackedInline):
#    model = Resim
#    extra = 3

#class AlbumAdmin(admin.ModelAdmin):
#    inlines = [ResimInline]

#admin.site.register(Album, AlbumAdmin)
admin.site.register(Yazar)
admin.site.register(Yazi)
