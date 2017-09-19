from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User
# Register your models here.


class UserAdmin(UA):

    fieldsets = (
        ('Datos de Cuenta', {
            'fields': ('email', 'password', 'is_active', 'is_staff')
        }), ('Datos personales', {
            'fields': ('nombre', 'apaterno', 'amaterno', 'numero_celular', 'genero',
                       'fecha_nacimiento')

        }),

        ('Grupos', {
            'fields': ('groups',)
        }),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def username(self, instance):
        return instance.email

    def user_first_name(self, instance):
        return instance.nombre

    def user_last_name(self, instance):
        return instance.apaterno

    list_display = ('email', 'user_first_name', 'user_last_name', 'is_active')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
