from django.db import models

class ProductItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='main//static//img')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Order_qq(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order for {self.first_name} - {self.last_name} - {self.product.name} - {self.quantity}"



