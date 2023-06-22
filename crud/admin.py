from django.contrib import admin

# Register your models here.

# class TipoClienteAdmin(admin.ModelAdmin):
#     readonly_fields = ('idTipoCliente','created_at','updated_at')
#     list_display = ('idTipoCliente','nombreTC')
#     ordering = ('idTipoCliente',)

# class ClienteAdmin(admin.ModelAdmin):
#     readonly_fields = ('created_at','updated_at')
#     list_display = ('rutCliente','dvRutCliente','nombreCliente','telefonoCliente','emailCliente','idTipoCliente')
#     ordering = ('rutCliente',)

# class TipoProductoAdmin(admin.ModelAdmin):
#     readonly_fields = ('idTipoProducto','created_at','updated_at')
#     list_display = ('idTipoProducto','nombreTP')
#     ordering = ('idTipoProducto',)

# class ProductoAdmin(admin.ModelAdmin):
#     readonly_fields = ('idProducto','created_at','updated_at')
#     list_display = ('idProducto','nombreProducto','precioProducto','stockProducto','idTipoProducto')
#     ordering = ('idProducto','idTipoProducto',)


# admin.site.register(TipoCliente,TipoClienteAdmin)
# admin.site.register(Cliente,ClienteAdmin)
# admin.site.register(TipoProducto,TipoProductoAdmin)
# admin.site.register(Producto,ProductoAdmin)

