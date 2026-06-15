from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Holiday)
admin.site.register(Payslip)