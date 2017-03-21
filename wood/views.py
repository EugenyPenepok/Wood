from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from wood.models import *

path_prefix = 'wood/static/'


def index(_request):
    return render(_request, 'index.html')


def get_category(_request):
    categories = Category.objects.all()
    context = {"category": categories}
    return render(_request, "category.html", context)


def get_category_content(_request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category_id=category_id)
    context = {"product": products, "category": category}
    return render(_request, "list.html", context)


def get_product_add(_request, category_id):
    if _request.method == 'GET':
        covers = Coating.objects.all()
        materials = Material.objects.all()
        sizes = Size.objects.all()
        context = {"category_id": category_id, "covers": covers, "materials": materials, "sizes": sizes}
        return render(_request, 'addproduct.html', context)
    elif _request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        product = Product(name=_request.POST['name'],
                          description=_request.POST['comment'],
                          category_id=category)
        product.save()
        material = Material.objects.get(pk=_request.POST['materials'])
        coating = Coating.objects.get(pk=_request.POST['covers'])
        size = Size.objects.get(pk=_request.POST['sizes'])
        concrete_product = ConcreteProduct(product=product,
                                           material=material,
                                           coating=coating,
                                           size=size,
                                           price=_request.POST['price'],
                                           number=_request.POST['amount'],
                                           time_production=_request.POST['time'])
        concrete_product.save()
        context = {"category_id": category_id, "product": product}
        return render(_request, "product.html", context)


def category_delete(_request, category_id):
    category = Category.objects.get(pk=category_id)
    category.image.delete(save=True)
    category.delete()
    return redirect('category')


def category_add(request):
    if request.method == 'GET':
        return render(request, 'addcategory.html')
    elif request.method == 'POST':
        image_file = (request.FILES['image'])
        category = Category(name=request.POST['name'],
                            description=request.POST['comment'],
                            image=image_file)
        category.save()
        return redirect('category')


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
        return redirect('category')
    else:
        context = {"category": category}
        return render(request, 'editcategory.html', context)


def get_orders(request):
    if request.method == 'GET':
        return render(request, 'order.html')
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
    context = {'category_id': category_id, 'product': product}
    return render(request, 'product.html', context)
  
  
def registration(request):
    if request.method == 'GET':
        return render(request, 'register.html')
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
