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

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)$', views.view_product, name='view_product'),
    url(r'^category/(?P<category_id>[0-9]+)/product/create$', views.create_product, name='create_product'),
    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/delete$',
        views.delete_product, name='delete_product'),

    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/concrete/create$',
        views.create_concrete_product, name='concrete_product_create'),
    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/concrete/view$',
        views.view_concrete_products, name='view_concrete_products'),
    url(r'^category/(?P<category_id>[0-9]+)/product/(?P<product_id>[0-9]+)/concrete/(?P<concrete_product_id>[0-9]+)/delete$',
        views.delete_concrete_product, name='delete_concrete_product'),

    url(r'^material/create$', views.create_material, name='material_create'),
    url(r'^material/(?P<material_id>[0-9]+)/edit', views.edit_material, name='material_edit'),
    url(r'^material/(?P<material_id>[0-9]+)/delete', views.delete_material, name='material_delete'),
    url(r'^materials/$', views.view_materials, name='get_materials'),

    url(r'^coating/create$', views.create_coating, name='coating_create'),
    url(r'^coating/(?P<coating_id>[0-9]+)/edit', views.edit_coating, name='coating_edit'),
    url(r'^coating/(?P<coating_id>[0-9]+)/delete', views.delete_coatings, name='coating_delete'),
    url(r'^coatings/$', views.view_coatings, name='get_coatings'),

    url(r'^size/create$', views.create_size, name='size_create'),
    url(r'^size/(?P<size_id>[0-9]+)/edit', views.edit_size, name='size_edit'),
    url(r'^size/(?P<size_id>[0-9]+)/delete', views.delete_size, name='size_delete'),
    url(r'^sizes$', views.get_sizes, name='get_sizes'),

    url(r'^profile/view$', views.view_profile, name='view_profile'),

    url(r'^orders/view$', views.view_orders, name='view_orders'),


    url(r'^category/[0-9]+/product/(?P<product_id>[0-9]+)/ajax_update_product',
        views.ajax_update_product, name='ajax_update_product'),

    url(r'^profile/change_password', views.change_password, name='change_password'),
    url(r'^order/(?P<order_id>[0-9]+)/attachments', views.download_attachments, name='download_attachments'),
    url(r'^order/(?P<order_id>[0-9]+)/requirements', views.get_requirements, name='get_requirements'),
]
