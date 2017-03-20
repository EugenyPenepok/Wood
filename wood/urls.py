from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_values, name='index'),
    url(r'^order$', views.get_orders, name='order'),
    url(r'^category$', views.get_category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/delete', views.category_delete, name='category_delete'),
    url(r'^category/add$', views.category_add, name='category_add'),
    url(r'^category/(?P<category_id>[0-9]+)/edit$', views.category_edit, name='category_edit'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.get_category_content, name='category_content'),

    url(r'^category/(?P<category_id>[0-9]+)/product/add$', views.get_product_add, name='product_add')

]
