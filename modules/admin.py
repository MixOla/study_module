from django.contrib import admin

from modules.models import Module


class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "number", "description")
    search_fields = ("title", "number", 'description')


admin.site.register(Module, ModuleAdmin)