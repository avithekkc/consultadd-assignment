from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=30)

    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'student'
