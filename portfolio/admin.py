from django.contrib import admin

# Register your models here.
from .models import Project
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display =('title', 'descripcion', 'image', 'created', 'updated', 'url')


admin.site.register(Project,ProjectAdmin)