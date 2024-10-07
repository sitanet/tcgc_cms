from django.db import models
from accounts.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name



class Asset_Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class AssetCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(AssetCategory, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    asset_class = models.ForeignKey(Asset_Class, on_delete=models.CASCADE, default=1)
    unit = models.IntegerField()
    percent_dep  = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    Total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    serial_number = models.CharField(max_length=250)
    condition = models.CharField(max_length=50, choices=[('New', 'New'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')])
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MaintenanceRecord(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='maintenance_records')
    maintenance_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.asset.name} - {self.maintenance_date}"




