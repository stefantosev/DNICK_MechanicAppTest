from django.contrib import admin
from mechanic_app.models import *

# Register your models here.

class WorkshopAdmin(admin.ModelAdmin):
    pass
    #Откако една работилница ќе биде зачувана, истата не може да се промени и избрише
    # def has_change_permission(self, request, obj=None):
    #     if not request.user.has_perm('yourapp.change_workshop'):
    #         return False
    #     return super().has_change_permission(request, obj)
    #
    # def has_delete_permission(self, request, obj=None):
    #     if not request.user.has_perm('yourapp.delete_workshop'):
    #         return False
    #     return super().has_delete_permission(request, obj)

class ScheduleAdmin(admin.ModelAdmin):
    pass
    # #При креирањето на поправката, корисникот се доделува автоматски според најавениот корисник
    # def save_model(self, request, obj, form, change):
    #     if not obj.user:  # Assign user only if it's not already assigned
    #         obj.user = request.user
    #     super().save_model(request, obj, form, change)


class MechanicAdmin(admin.ModelAdmin):
    pass

class AutomobileAdmin(admin.ModelAdmin):
    pass


admin.site.register(ScheduledRepair, ScheduleAdmin)
admin.site.register(Manufacturer, MechanicAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Automobiles, AutomobileAdmin)
