from django.contrib import admin

from .models import student
class studentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'username','password')
    search_fields=('firstname','lastname')
admin.site.register(student)
