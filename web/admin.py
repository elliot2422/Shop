from django.contrib import admin

# Register your models here.

from .models import Categoria,Productos

admin.site.register(Categoria)
# admin.site.register(Productos)

@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'Categoria', 'fecha_registro')
    list_editable = ('precio',)