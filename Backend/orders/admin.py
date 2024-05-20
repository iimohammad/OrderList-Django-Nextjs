from django.contrib import admin
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'date', 'quantity', 'dedicated_supplier_status', 'public_supplier_status', 'related_group_status', 'guarantee_status')
    list_filter = ('dedicated_supplier_status', 'public_supplier_status', 'related_group_status', 'guarantee_status')
    search_fields = ('product', 'user__username')
    readonly_fields = ('date', 'user')

    def delete_all_orders(self, request, queryset):
        queryset.delete()
    delete_all_orders.short_description = "Delete selected orders"

admin.site.register(Order, OrderAdmin)
