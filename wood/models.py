from django.db import models


# Категория
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image_path = models.CharField(max_length=1000)


# Изделие
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)


# Покрытие
class Coating(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)


# Материал
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    amount = models.DecimalField(max_digits=13, decimal_places=3)


# Размер
class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    # Размеры в миллиметрах
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    # Вес в граммах
    weight = models.IntegerField()


# Тип доставки
class TypeOfDelivery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # Цена в копейках
    price = models.IntegerField()


# Клиент
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    postcode = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.patronymic


# Изделие с конкретными параметрами
class ConcreteProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # Цена в копейках
    price = models.IntegerField()
    number = models.IntegerField()
    time_production = models.DateTimeField()
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
    date = models.DateField()
    status = models.CharField(max_length=300)
    information = models.CharField(max_length=5000)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    type_of_delivery = models.ForeignKey(TypeOfDelivery, on_delete=models.PROTECT)


# Позиция в заказе
class PositionInOrder(models.Model):
    id = models.AutoField(primary_key=True)
    # Цена в копейках
    amount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    concrete_product = models.ForeignKey(ConcreteProduct, on_delete=models.PROTECT)


# Индивидальный заказ
class PersonalOrder(models.Model):
    id = models.AutoField(primary_key=True)
    requirements = models.CharField(max_length=5000)
    # !!! Нужно понять, как будут храниться приложения к индивидуальному заказу !!!
    attachments = None
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
