from django.contrib import admin
from .models import  ResponseOrders

@admin.register(ResponseOrders)
class ResponseOrdersAdmin(admin.ModelAdmin):
    list_display = ('user', 'response_date', 'order', 'price', 'deliver_time', 'quantity')
    search_fields = ('user', 'order__id')
    list_filter = ('user', 'response_date', 'order')

