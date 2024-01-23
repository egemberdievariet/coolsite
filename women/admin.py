from django.contrib import admin
from women.models import Women, Category


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'age')
    list_display_links = ('id', 'first_name')
    search_fields = ('bio', 'first_name')
    list_filter = ('nationality',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ist_display_links = ('id', 'name')
    search_fields = ('name',)

# Register your models here.
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)