from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'desc', 'complete') # add this


# Register your models here.
admin.site.register(Todo, TodoAdmin)