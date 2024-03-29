from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=200)

    def signup_email_exits(self):
        if Customer.objects.filter(email= self.email):
            return True
        else:
            return False

    @staticmethod
    def login_email_exits(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


class Complain(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=250)



class Subscribe_customer(models.Model):
    email = models.EmailField()
    coupon = models.CharField(max_length=30, blank=True, null=True)
