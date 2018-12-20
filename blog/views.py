# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Berita

# Create your views here.

def home(request):
    # beritas = Berita.objects.filter(kategori__nama='Biodata')
    beritas = Berita.objects.all()
    return render(request, 'index.html', {'beritas':beritas})


def biodata(request):
    Nama= "Selpisrimulyani"
    Kelas= "XI-RPL-3"
    Sekolah= "SMKN-4-Tasikmalaya"
    return render(request,'about.html',
    {
    'Nama':Nama,
    'Kelas':Kelas,
    'Sekolah':Sekolah
    })

def detil_berita(request, id_berita):
    berita = Berita.objects.get(id=id_berita)
    return render(request,'post.html', {'berita':berita})

def contact(request):
    return render(request,'contact.html')
