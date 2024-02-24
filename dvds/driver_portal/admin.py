from django.contrib import admin
from .models import LessonPricing

# Register your models here.


class PricingAdmin(admin.ModelAdmin):
    """
        Lesson pricing admin 
    """

    list_display = ('manual_hourly',)


admin.site.register(LessonPricing, PricingAdmin)
