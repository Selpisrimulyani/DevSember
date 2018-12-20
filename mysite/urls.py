from django.conf.urls import url
from django.contrib import admin
from blog.views import home, detil_berita, biodata, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/', biodata),
    url(r'^contact/', contact),
    url(r'^(\d+)$', detil_berita),

]
