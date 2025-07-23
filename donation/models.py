from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ]
    ORGAN_TYPES = [
        ('Kidney', 'Kidney'), ('Heart', 'Heart'), ('Liver', 'Liver'),
        ('Lung', 'Lung'), ('Pancreas', 'Pancreas'), ('Blood Only', 'Blood Only')
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPES)
    organ = models.CharField(max_length=50, choices=ORGAN_TYPES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.blood_group} | {self.organ}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    is_donor = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hospital_images/')
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class HospitalFormSubmission(models.Model):
    FORM_TYPE_CHOICES = [('donate', 'Donate'), ('need', 'Need Donor')]
    
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=10, choices=FORM_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
