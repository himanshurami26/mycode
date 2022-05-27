from unicodedata import category
from django.db import models

# Create your models here.

# class Country(models.Model):


class ContryDetails(models.Model):
    country_name = models.CharField(max_length=300)    

    def __str__(self):
        return self.country_name

class Category(models.Model):
    category_name = models.CharField(max_length=300)
    

    def __str__(self):
        return self.category_name


class StudentDetails(models.Model):
    country_id = models.ForeignKey('ContryDetails', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    heading =  models.CharField(max_length=300)
    peragraph = models.TextField()

    def __str__(self):
        return self.heading

# CREATE TABLE student_Data (StudentName VARCHAR (255) NOT NULL, StudentAge  INT NOT NULL, StudentGrade VARCHAR (255) NOT NULL);

class filedetails(models.Model):
    file = models.CharField(max_length=255)
    service_type_name = models.CharField(max_length=300)
    letter_type_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    country_name = models.CharField(max_length=300)

    def __str__(self):
        return self.file


