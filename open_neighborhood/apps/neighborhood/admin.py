from django.contrib import admin
from .models import Person , Resident, House, Block, Employee, Role_employee, Role
# Register your models here.

admin.site.register(Person)
admin.site.register(Resident)
admin.site.register(House)
admin.site.register(Block)
admin.site.register(Employee)
admin.site.register(Role_employee)
admin.site.register(Role)