from django.contrib import admin
from .models import GearBox, Promotion, Support

# Register your models here.


class Promotion_Admin(admin.ModelAdmin):
    """
        Locations Admin
    """

    list_display = ('promotion', 'friendly_name')


class Gearbox_Admin(admin.ModelAdmin):
    """
        Locations Admin
    """

    list_display = ('gearbox', 'friendly_name')


class Support_Admin(admin.ModelAdmin):
    """
        Support Form Admin
    """

    list_display = ('name', 'email', 'number', 'location')


admin.site.register(Promotion, Promotion_Admin)
admin.site.register(GearBox, Gearbox_Admin)
admin.site.register(Support, Support_Admin)
