from django.contrib import admin

from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Recipe, RecipeAdmin)



# Register your models here.
