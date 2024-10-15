from django.db import models

# Create your models here.
from django.db import models  # Import the models module to create database models
from django.contrib.auth.models import User  # Import the User model for user management



class currency_notes(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    denomination = models.CharField(max_length=50, null=True, blank=True)  # Optional
    material = models.CharField(max_length=50, null=True, blank=True)      # Optional
    year_issued = models.IntegerField(null=True, blank=True)                # Optional
    quantity_produced = models.IntegerField(null=True, blank=True)          # Optional

    def __str__(self):
        return self.denomination  # Display denomination in dropdown

    
    
class production_records(models.Model):
    id = models.AutoField(primary_key=True)
    currency_notes = models.ForeignKey(currency_notes, on_delete= models.CASCADE)
    date_produced = models.DateField()
    batch_number = models.CharField(max_length=50, unique=True)
    quantity_produced = models.IntegerField()
    
    def __str__(self):
        return f"Batch {self.batch_number} - {self.date_produced}"
    
    
class inventory(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    currency_notes = models.ForeignKey(currency_notes, on_delete=models.CASCADE)
    quantity_available = models.IntegerField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.currency_note} - {self.location}"
    
    