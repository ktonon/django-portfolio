from django.contrib import admin
from portfolio.models import *

admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(ProjectFile)
admin.site.register(ProjectImage)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0

class ProjectFileInline(admin.TabularInline):
    model = ProjectFile
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'url', 'start_date', 'end_date')}),
        ('Details', {'fields': ('category', 'skills', 'pull_quote', 'short_description', 'description')}),
    )
    search_fields = ('name', 'category__name')
    list_display = ('name', 'start_date', 'category')
    list_filter = ('category', 'skills')
    filter_horizontal = ('skills',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'start_date'
    inlines = (ProjectImageInline, ProjectFileInline)
admin.site.register(Project, ProjectAdmin)
