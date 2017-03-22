from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# Create your views here.
from wood.models import *

path_prefix = 'wood/static/'


def index(request):
    return render(request, 'index.html')


def get_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "catalog.html", context)


def get_products_in_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category_id=category_id)
    context = {"products": products, "category": category}
    return render(request, "products_in_category.html", context)


def category_delete(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.image.delete(save=True)
    category.delete()
    return redirect('get_categories')


def category_add(request):
    if request.method == 'GET':
        return render(request, 'create_category.html')
    elif request.method == 'POST':
        image_file = request.FILES['image']
        category = Category(name=request.POST['name'],
                            description=request.POST['comment'],
                            image=image_file)
        category.save()
        return redirect('get_categories')


def category_edit(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        image_file = request.FILES.get('image', False)
        if image_file:
            category.image.delete(save=True)
            category.image = image_file
        category.name = request.POST['name']
        category.description = request.POST['comment']
        category.save()
        return redirect('get_categories')
    else:
        context = {"category": category}
        return render(request, 'edit_category.html', context)


'''def product_add(request, category_id):
    if request.method == 'GET':
        covers = Coating.objects.all()
        materials = Material.objects.all()
        sizes = Size.objects.all()
        context = {"category_id": category_id, "covers": covers, "materials": materials, "sizes": sizes}
        return render(request, 'create_product.html', context)
    elif request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        product = Product(name=request.POST['name'],
                          description=request.POST['comment'],
                          category_id=category)
        product.save()
        # material = Material.objects.get(pk=request.POST['materials'])
        # coating = Coating.objects.get(pk=request.POST['covers'])
        # size = Size.objects.get(pk=request.POST['sizes'])
        # concrete_product = ConcreteProduct(product=product,
                                           # material=material,
                                           # coating=coating,
                                           # size=size,
                                           # price=request.POST['price'],
                                           # number=request.POST['amount'],
                                           # time_production=request.POST['time'])
        # concrete_product.save()
        context = {"category_id": category_id, "product": product}
        return render(request, "product.html", context)
'''


def product_create(request, category_id):
    if request.method == 'GET':
        context = {"category_id": category_id}
        return render(request, 'create_product.html', context)
    elif request.method == 'POST':
        image_file = request.FILES['image']
        category = Category.objects.get(pk=category_id)
        product = Product(category=category,
                            name=request.POST['name'],
                            description=request.POST['comment'],
                            product_image=image_file)
        product.save()
        return redirect('get_categories')


def get_orders(request):
    if request.method == 'GET':
        return render(request, 'create_personal_order.html')
    elif request.method == 'POST':
        client = Client.objects.filter(name=request.POST['name'],
                                       surname=request.POST['surname'],
                                       patronymic=request.POST['patronymic'],
                                       telephone=request.POST['telephone'],
                                       email=request.POST['email'])
        if not client:
            client = Client(name=request.POST['name'],
                            surname=request.POST['surname'],
                            patronymic=request.POST['patronymic'],
                            telephone=request.POST['telephone'],
                            email=request.POST['email'])
            client.save()
        else:
            client = client[0]
        file = (request.FILES['attachments'])
        if client:
            save_path = "upload/personal_orders/" + file.name
            upload_path = default_storage.save(path_prefix + save_path, ContentFile(file.read()))
            real_path = upload_path.split(path_prefix)[1]
            personal_order = PersonalOrder(client=client,
                                           requirements=request.POST['requirements'],
                                           attachments=real_path)
            personal_order.save()
            return redirect('index')


def get_product(request, category_id, product_id):
    product = Product.objects.get(pk=product_id)
    concrete_products = ConcreteProduct.objects.filter(product_id=product_id)
    materials = Material.objects.all()
    for material in materials:
        remove = True
        for p in concrete_products:
            if material.id == p.material_id:
                remove = False
        if remove:
            materials.filter(id=material.id)
    sizes = Size.objects.all()
    coatings = Coating.objects.all()
    context = {'category_id': category_id,
               'product': product,
               'concrete_products': concrete_products,
               'materials': materials,
               'sizes': sizes,
               'coatings': coatings,
               }
    return render(request, 'product.html', context)


def concrete_product_create(request, category_id, product_id):
    if request.method == 'GET':
        materials = Material.objects.all()
        sizes = Size.objects.all()
        coatings = Coating.objects.all()
        context = {'category_id': category_id,
                   'product_id': product_id,
                   'materials': materials,
                   'sizes': sizes,
                   'coatings': coatings
                   }
        return render(request, 'create_concrete_product.html', context)
    elif request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        material = Material.objects.get(pk=request.POST['materials'])
        coating = Coating.objects.get(pk=request.POST['coatings'])
        size = Size.objects.get(pk=request.POST['sizes'])
        concrete_product = ConcreteProduct(product=product,
                                           price=request.POST['price'],
                                           number=request.POST['amount'],
                                           time_production=request.POST['time'],
                                           material=material,
                                           coating=coating,
                                           size=size)
        concrete_product.save()
        return redirect('get_categories')


def registration(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'],
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'],
                                        )
        user.save()
        client = Client(user=user,
                        telephone=request.POST['telephone'],
                        skype=request.POST['skype'],
                        postcode=request.POST['postcode'],
                        address=request.POST['address'])
        client.save()
        return redirect('index')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'auth.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user.is_active:
            login(request, user)
        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')


def ajax_info_about_product(request, category_id, product_id):
    name_material = request.GET['material']
    material = Material.objects.get(name=name_material)
    product = Product.objects.get(pk=product_id)
    concrete_products = ConcreteProduct.objects.filter(material=material).filter(product=product)
    data = dict()
    if concrete_products:
        data['form_is_valid'] = True
    else:
        data['none'] = True
    return JsonResponse(data)


def material_create(request):
    if request.method == 'GET':
        return render(request, 'create_material.html')
    elif request.method == 'POST':
        material = Material(name=request.POST['name'],
                            description=request.POST['description'],
                            amount=request.POST['amount'])
        material.save()
        return redirect('get_categories')


def coating_create(request):
    if request.method == 'GET':
        return render(request, 'create_coating.html')
    elif request.method == 'POST':
        coating = Coating(name=request.POST['name'],
                            description=request.POST['description'])
        coating.save()
        return redirect('get_categories')


def size_create(request):
    if request.method == 'GET':
        return render(request, 'create_size.html')
    elif request.method == 'POST':
        size = Size(length=request.POST['length'],
                    width=request.POST['width'],
                    height=request.POST['height'],
                    weight=request.POST['weight'])
        size.save()
        return redirect('get_categories')
