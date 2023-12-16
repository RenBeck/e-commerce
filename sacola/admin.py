from django.contrib import admin
from . import models


class ItemSacolaInline(admin.TabularInline):
    model = models.ItemSacola
    extra = 1


class SacolaAdmin(admin.ModelAdmin):
    inlines = [
        ItemSacolaInline
    ]


admin.site.register(models.Sacola, SacolaAdmin)
admin.site.register(models.ItemSacola)
