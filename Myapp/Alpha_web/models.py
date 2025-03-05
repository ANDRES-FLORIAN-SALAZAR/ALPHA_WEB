from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}(s) on {self.order_date}"
        class Customer(models.Model):
            first_name = models.CharField(max_length=50)
            last_name = models.CharField(max_length=50)
            email = models.EmailField(unique=True)
            phone = models.CharField(max_length=20, blank=True, null=True)
            address = models.TextField(blank=True, null=True)

            def __str__(self):
                return f"{self.first_name} {self.last_name}"

        class Order(models.Model):
            product = models.ForeignKey(Product, on_delete=models.CASCADE)
            customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
            quantity = models.IntegerField()
            order_date = models.DateTimeField(auto_now_add=True)
            class Meta:
                ordering = ['-order_date']
            def __str__(self):
                return f"Order of {self.quantity} {self.product.name}(s) by {self.customer.first_name} on {self.order_date}"