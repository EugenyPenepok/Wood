from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$wood/', views.index, name='index'),
]
