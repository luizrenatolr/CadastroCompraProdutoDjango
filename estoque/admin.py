from django.contrib import admin
from .models import Produto, Compra

# Register your models here.

admin.site.register(Produto)
admin.site.register(Compra)