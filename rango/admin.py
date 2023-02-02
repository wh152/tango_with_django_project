from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, PageAdmin)
