from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.
@admin.register(User)
class User(DjangoUserAdmin):
    # Cuando se edita el usuario
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('area_interes', 'ocupacion')}),
    )

    # Cuando se crea un nuevo usuario
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('area_interes', 'ocupacion')}),
    )