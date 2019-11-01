from django.contrib import admin
from .models import ConstantField
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.unregister(User),
UserAdmin.list_display = ('username', 'password')
admin.site.register(User, UserAdmin)
admin.site.register(ConstantField)

