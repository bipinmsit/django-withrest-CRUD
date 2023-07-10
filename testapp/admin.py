from django.contrib import admin
from testapp.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "emp_name", "emp_sal", "emp_id", "emp_addr"]


admin.site.register(Employee, EmployeeAdmin)
