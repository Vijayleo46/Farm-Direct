from django.db import models
from django.contrib.auth.models import User as Person


# Extend login model if needed, or use Django's User model directly.

class Login(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class UserTable(models.Model):
    login = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='user_photos/')
    status = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class FarmerTable(models.Model):
    login = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='farmer_photos/')
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=50)



class DeliveryStaff(models.Model):
    login = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    drivinglicense = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=50)



class ProductTable(models.Model):
    farmer = models.ForeignKey(FarmerTable, on_delete=models.CASCADE)
    productname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='product_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()


class ComplaintTable(models.Model):
    login = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    complaints = models.TextField()
    reply = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('replied', 'Replied'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


class Feedback(models.Model):
    date = models.DateField()
    feedback = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)


class ChatTable(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    fromid = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_messages')
    toid = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_messages')


class OrderMain(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    farmer = models.ForeignKey(FarmerTable, on_delete=models.CASCADE)


class OrderSub(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    ordermain = models.ForeignKey(OrderMain, on_delete=models.CASCADE)


class AssignTable(models.Model):
    ordermain = models.ForeignKey(OrderMain, on_delete=models.CASCADE)
    date = models.DateField()
    deliverystaff = models.ForeignKey(DeliveryStaff, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)


class Cart(models.Model):
    date = models.DateField()
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Payment(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=50)
    ordermain = models.ForeignKey(OrderMain, on_delete=models.CASCADE)
    totalamount = models.DecimalField(max_digits=10, decimal_places=2)
