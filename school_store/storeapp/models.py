from django.db import models

# Create your models here.


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
    ]
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    purpose = models.CharField(max_length=20,default='Enquiry', choices=PURPOSE_CHOICES)



    def __str__(self):
        return self.name



