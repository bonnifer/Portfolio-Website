from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^page-analyser/', include('page_analyser.urls')),
    url(r'^google6430b1c1c5f4d50f\.html$', lambda r: HttpResponse("google-site-verification: google6430b1c1c5f4d50f.html", content_type="text/plain")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
