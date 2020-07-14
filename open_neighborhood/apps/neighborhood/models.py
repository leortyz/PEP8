from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=20, help_text="This is field for the numbre of identification card")
    name = models.CharField(max_length=100, help_text="This is a field for the person name")
    birth = models.DateField(help_text="This is a field for the date that was born")
    status = models.BooleanField(help_text="This is a field for the status of the person")
    email = models.CharField(max_length=100,null=False , default=' ' ,help_text="This is a field for person email")
    password = models.CharField(max_length=12,null=False, default= ' ',help_text="This is a field for person password")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the person was created")

    def __str__(self):
        return self.name

class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, help_text="This is a field for the block name")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the block was created")

    def __str__(self):
        return self.block_id


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    block_id = models.ForeignKey('Block', on_delete=models.CASCADE, help_text="This is a field for block that contains the house")
    phone = models.CharField(max_length=10, help_text="This is a field for the house phone")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the house was created")

    def __str__(self):
        return self.house_id


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person',on_delete=models.CASCADE, help_text="This is a field for the person number")
    house_id = models.ForeignKey('House',on_delete=models.CASCADE, help_text="This is a field for the house number where the resident lives")
    landlord = models.BooleanField(help_text="This is a field that identifies if the resident owns the home")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the resident was created")

    def __str__(self):
        return self.resident_id

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person',on_delete=models.CASCADE,  help_text="This is a field for the person number of the employee")
    phone = models.CharField(max_length=10, help_text="This is a field for the number of the employee")
    home_address = models.CharField(max_length=100,  help_text="This is a field for the ubication where the employee lives")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the employee was created")

    def __str__(self):
        return self.employee_id
    
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False, help_text="This is a field for the house phone")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify that date that of the role was created")

    def __str__(self):
        return self.role_id

class Role_employee(models.Model):
    re_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('Employee',on_delete=models.CASCADE, help_text="This is a field for the employee number")
    role_id = models.ForeignKey('Role',on_delete=models.CASCADE,help_text="This is a field for the role number")
    created_at = models.DateTimeField(default=timezone.now,help_text="This is a field specify date that of the relation between the role and employee was created")

    def __str__(self):
        return self.re_id


