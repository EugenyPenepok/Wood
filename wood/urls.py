from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order$', views.get_orders, name='order'),

    url(r'^registration$', views.registration, name='registration'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),

    url(r'^category$', views.get_categories, name='get_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/delete', views.category_delete, name='category_delete'),
    url(r'^category/add$', views.category_add, name='category_add'),
    url(r'^category/(?P<category_id>[0-9]+)/edit$', views.category_edit, name='category_edit'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.get_products_in_category, name='category_content'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)$', views.get_product, name='product'),
    url(r'^category/(?P<category_id>[0-9]+)/product/create$', views.product_create, name='product_create'),
    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/ajax_info_about_product$',
        views.ajax_info_about_product, name='ajax_info_about_product'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/concrete/create$',
        views.concrete_product_create, name='concrete_product_create'),

    url(r'^material/create$', views.material_create, name='material_create'),
    url(r'^coating/create$', views.coating_create, name='coating_create'),
    url(r'^size/create$', views.size_create, name='size_create'),

]
