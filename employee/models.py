from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    sign_in=models.TimeField()
    sign_out=models.TimeField(null=True,blank=True)

    def __str__(self):
        return self.employee.user.username


class Leave(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    reason=models.TextField()
    from_date=models.DateField()
    to_date=models.DateField()

    status=models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return self.employee.user.username


class Holiday(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.name


class Payslip(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    month=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.month