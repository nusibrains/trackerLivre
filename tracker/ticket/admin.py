from django.contrib import admin
from .models import Task

# on add le model Task pour le voir dans l'admin


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'schedule_date', 'colored_due_date')


admin.site.register(Task, TaskAdmin)
