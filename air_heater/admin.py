from django.contrib import admin
from .models import Temperature



class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['value', 'created_at']
    list_filter = ['created_at']
    search_fields = ['value']
    ordering = ['-created_at']
    readonly_fields = ('created_at',)



admin.site.register(Temperature, TemperatureAdmin)
