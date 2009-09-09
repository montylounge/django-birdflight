from django.contrib import admin
from birdflight.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['codename','description']
    search_fields = ['codename']

admin.site.register(Project,ProjectAdmin)