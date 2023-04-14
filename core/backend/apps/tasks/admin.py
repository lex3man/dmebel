from django.contrib import admin
from .models import Project, CheckPoint, Task, Report


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('caption',)


@admin.register(CheckPoint)
class CheckpointAdmin(admin.ModelAdmin):
    list_display = ('caption', 'date')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('caption', 'deadline', 'maker', 'status')
    list_filter = ('maker', 'status')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('caption', 'date')
    search_fields = ('caption', 'date', 'content')
