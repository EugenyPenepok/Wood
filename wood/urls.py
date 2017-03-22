from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^create_personal_order$', views.create_personal_order, name='create_personal_order'),

    url(r'^registration$', views.registration, name='registration'),
    url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^logout_user$', views.logout_user, name='logout_user'),

    url(r'^category$', views.get_categories, name='get_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/delete', views.delete_category, name='category_delete'),
    url(r'^category/add$', views.create_category, name='category_add'),
    url(r'^category/(?P<category_id>[0-9]+)/edit$', views.edit_category, name='category_edit'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.get_products_in_category, name='category_content'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)$', views.get_product, name='product'),
    url(r'^category/(?P<category_id>[0-9]+)/product/create$', views.create_product, name='product_create'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/ajax_update_product',
        views.ajax_update_product, name='ajax_update_product'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/concrete/create$',
        views.create_concrete_product, name='concrete_product_create'),

    url(r'^material/create$', views.create_material, name='material_create'),
    url(r'^coating/create$', views.create_coating, name='coating_create'),
    url(r'^size/create$', views.create_size, name='size_create'),

    url(r'^profile/view$', views.view_profile, name='view_profile'),

    url(r'^orders/view$', views.view_orders, name='view_orders'),
]
