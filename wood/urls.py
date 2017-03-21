from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order$', views.get_orders, name='order'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),
    url(r'^category$', views.get_category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/delete', views.category_delete, name='category_delete'),
    url(r'^category/add$', views.category_add, name='category_add'),
    url(r'^category/(?P<category_id>[0-9]+)/edit$', views.category_edit, name='category_edit'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.get_category_content, name='category_content'),
    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)$', views.get_product, name='product'),
    url(r'^category/(?P<category_id>[0-9]+)/product/add$', views.product_add, name='product_add'),
]
