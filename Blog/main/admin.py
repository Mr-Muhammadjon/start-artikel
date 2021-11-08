from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','id']
#     prepopulated_fields = {'slug':('name',)}


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title','id']
#     prepopulated_fields = {'slug':('title',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
