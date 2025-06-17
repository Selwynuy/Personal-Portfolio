"""
Admin configuration for the main app.
"""
from django.contrib import admin
from .models import Project, SkillCategory, Skill, Timeline


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'github_url']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'event_type']
    list_filter = ['event_type']
    search_fields = ['title', 'description'] 