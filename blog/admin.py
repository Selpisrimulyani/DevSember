from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Berita, Kategori

# Register your models here.
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['judul', 'tanggal', 'kategori', 'publish']
    list_filter = ['kategori', 'publish']
    list_per_page = 20
    search_fields = ['judul', 'kategori__nama']

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['nama', 'keterangan']
    search_filter = ['keterangan']
    list_per_page = 20
    search_fields = ['nama']

admin.site.register(Berita, BeritaAdmin)
admin.site.register(Kategori)
