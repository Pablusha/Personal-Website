from django.contrib import admin

from .models import Projects
# Register your models here.
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Projects