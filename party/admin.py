from django.contrib import admin

from party.models import Party, MenuItems, NewOrder


# Register your models here.


class MenuItemsAdmin(admin.StackedInline):
    fields = ('party', 'description')
    model = MenuItems


class PartyAdmin(admin.ModelAdmin):
    fields = ('name', 'status')
    list_display = ('name', 'status', 'created')
    list_filter = ('status',)
    inlines = [MenuItemsAdmin]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(status=1)


class NewOrdersAdmin(admin.ModelAdmin):
    fields = ('party', 'item', 'status')
    list_display = ('party', 'item', 'status', 'employee', 'created')
    list_filter = ('party', 'status')

    def save_model(self, request, obj, form, change):
        if obj and obj.employee_id != None and obj.employee != request.user:
            pass
        else:
            obj.employee = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(employee_id=request.user.id)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request)
        if obj and obj.status == NewOrder.CLOSED:
            fields = ('status', 'party', 'item', *fields)
        else:
            if not request.user.is_superuser:
                fields = ('status', *fields)
        return fields


#
# class OrderItemsAdmin(admin.StackedInline):
#     fields = ('item', 'order')
#     list_display = ('item', 'order')
#     model = OrderItems
#
#     def get_readonly_fields(self, request, obj=None):
#         fields = super().get_readonly_fields(request)
#         if obj:
#             if not request.user.is_superuser and obj.status == Orders.CLOSED:
#                 fields = ('item', 'order', *fields)
#         return fields
#
#     def has_delete_permission(self, request, obj=None):
#         if obj and obj.status == Orders.CLOSED:
#             return False
#
#
# class OrdersAdmin(admin.ModelAdmin):
#     fields = ('party', 'status')
#     list_display = ('party', 'status', 'employee')
#     list_filter = ('party', 'status')
#     inlines = [OrderItemsAdmin]
#
#     # readonly_fields = (get_readonly_fields)
#
#     def save_model(self, request, obj, form, change):
#         obj.employee = request.user
#         super().save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(employee_id=request.user.id)
#
#     def get_readonly_fields(self, request, obj=None):
#         fields = super().get_readonly_fields(request)
#         if obj and obj.status == Orders.CLOSED:
#             fields = ('status', 'party', *fields)
#         else:
#             if not request.user.is_superuser:
#                 fields = ('status', *fields)
#         return fields


admin.site.register(Party, PartyAdmin)
# admin.site.register(Orders, OrdersAdmin)
admin.site.register(NewOrder, NewOrdersAdmin)
