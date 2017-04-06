import datetime

from django.contrib.auth.models import User
from django.db import models


# Категория
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.name


# Изделие
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    product_image = models.ImageField(upload_to='images/products/')
    visible = models.BooleanField(False)

    def __str__(self):
        return self.name

    def is_visible(self):
        return self.visible


# Покрытие
class Coating(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


# Материал
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=3)

    def __str__(self):
        return self.name


# Размер
class Size(models.Model):
    id = models.AutoField(primary_key=True)
    # Размеры в миллиметрах
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    # Вес в граммах
    weight = models.IntegerField()

    def __str__(self):
        return str(self.length) + 'x' + str(self.width) + 'x' + str(self.height)


# Клиент
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, unique=True)
    telephone = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    postcode = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


# Изделие с конкретными параметрами
class ConcreteProduct(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    number = models.IntegerField()
    time_production = models.IntegerField(blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    coating = models.ForeignKey(Coating, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


# Изображение
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1000)
    concrete_product = models.ForeignKey(ConcreteProduct, on_delete=models.PROTECT)


# Заказ
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    status_choise = (
        ('Отменен', 'Отменен'),
        ('Обрабатывается', 'Обрабатывается'),
        ('Выполнен', 'Выполнен'),
    )
    status = models.CharField(max_length=15, choices=status_choise, default='Обрабатывается')
    delivery_address = models.CharField(max_length=2000, blank=True, null=True)
    payment = (
        ('Наличный расчет', 'Наличный расчет'),
        ('Безналичный расчет', 'Безналичный расчет')
    )
    payment_type = models.CharField(max_length=50, choices=payment)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    need_delivery = models.BooleanField(default=False)
    date_delivery = models.DateTimeField()
    cost_delivery = models.IntegerField()


# Позиция в заказе
class PositionInOrder(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    price = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    concrete_product = models.ForeignKey(ConcreteProduct, on_delete=models.PROTECT)


# Индивидуальный заказ
class PersonalOrder(models.Model):
    id = models.AutoField(primary_key=True)
    requirements = models.CharField(max_length=5000)
    attachments = models.FileField(upload_to='archives/personal_orders/')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    need_delivery = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    status_choise = (
        ('Изготовлен', 'Изготовлен'),
        ('Отменен', 'Отменен'),
        ('Обрабатывается', 'Обрабатывается')
    )
    status = models.CharField(max_length=50, choices=status_choise, default='Обрабатывается')
    payment = (
        ('Наличный расчет', 'Наличный расчет'),
        ('Безналичный расчет', 'Безналичный расчет')
    )
    payment_type = models.CharField(max_length=50, choices=payment)


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def add_concrete_product(self, concrete_product, quantity=1, update=False):
        concrete_product_id = str(concrete_product.id)
        if str(concrete_product_id) not in self.cart:
            self.cart[concrete_product_id] = 0
        if update:
            self.cart[concrete_product_id] = quantity
        else:
            self.cart[concrete_product_id] += quantity
        self.save()

    def get_summary_price(self):
        summary = 0
        for cp_id, quantity in self.cart.items():
            cp = ConcreteProduct.objects.get(pk=cp_id)
            summary += cp.price*quantity
        return summary

    def remove(self, concrete_product_id):
        if concrete_product_id in self.cart:
            del self.cart[concrete_product_id]
            self.save()

    def __len__(self):
        return sum(item for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.session.modified = True
