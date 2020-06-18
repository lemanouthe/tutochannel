from django.contrib import admin
from . import models
# Register your models here.

class SalonAdmin(admin.ModelAdmin):
    
    list_display = (
        'nom',
        'status',
        'date_upd',
        'date_add',
    )

    list_filter = (
        'status',
        'date_upd',
        'date_add',
    )

    actions = ('active','desactive')
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
            
    active.short_description = "activer Les salons selectionnés"
            
            
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
                
    desactive.short_description = "desactivés Les salons selectionnés"

class MessageAdmin(admin.ModelAdmin):
    
    list_display = (
        'author',
        'salon',
        'message',
        'status',
        'date_upd',
        'date_add',
    )

    list_filter = (
        'status',
        'date_upd',
        'date_add',
    )

    actions = ('active','desactive')
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request,"La selection a été activé avec succés")
            
    active.short_description = "activer Les messages selectionnés"
            
            
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request,"La selection a été desactivé avec succés")
                
    desactive.short_description = "desactivés Les messages selectionnés"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
_register(models.salon, SalonAdmin)