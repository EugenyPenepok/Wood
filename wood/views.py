from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.
from wood.models import *


def get_values(_request):
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
    covers = Coating.objects.all()
    materials = Material.objects.all()
    sizes = Size.objects.all()
    context = {"category_id": category_id, "covers": covers, "materials": materials, "sizes": sizes}
    return render(_request, 'addproduct.html', context)


def save_product(request):
    product = Product()
    return None


def category_delete(_request, category_id):
    Category.objects.get(pk=category_id).delete()
    return redirect('category')


def category_add(request):
    if request.method == 'GET':
        return render(request, 'addcategory.html')
    elif request.method == 'POST':
        image_file = (request.FILES['image'])
        path_prefix = 'wood/static/'
        save_path = "upload/category/" + image_file.name
        upload_path = default_storage.save(path_prefix + save_path, ContentFile(image_file.read()))
        real_path = upload_path.split(path_prefix)[1]
        category = Category(name=request.POST['name'],
                            description=request.POST['comment'],
                            image_path=real_path)
        category.save()
        return redirect('category')


def category_edit(request, category_id):
    category = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        image_file = request.FILES.get('image', False)
        if image_file:
            image_file = (request.FILES['image'])
            path_prefix = 'wood/static/'
            save_path = "upload/category/" + image_file.name
            upload_path = default_storage.save(path_prefix + save_path, ContentFile(image_file.read()))
            real_path = upload_path.split(path_prefix)[1]
            category.image_path = real_path
        category.name = request.POST['name']
        category.description = request.POST['comment']
        category.save()
        return redirect('category')
    else:
        context = {"category": category}
        return render(request, 'editcategory.html', context)
