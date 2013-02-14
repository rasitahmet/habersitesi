from haber.models import Haber, HaberResim
from django.contrib import admin

class ResimInline(admin.StackedInline):
    model = HaberResim
    extra = 3

class HaberAdmin(admin.ModelAdmin):
    inlines = [ResimInline]

admin.site.register(Haber, HaberAdmin)
