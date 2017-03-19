from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_values, name='index'),
    url(r'^gallery$', views.get_category, name='category')
]
