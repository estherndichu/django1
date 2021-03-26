from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
import os

urlpatterns=[
    url('^$',views.photos,name='photos'),
    url('^location/(?P<location>\w+)/', views.image_location, name='location'),
    url('^search/', views.search_results, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)