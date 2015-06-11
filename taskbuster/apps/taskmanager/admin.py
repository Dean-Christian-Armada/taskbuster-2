from django.contrib import admin
from . import models

# Register your models here.

class ProjectsInline(admin.TabularInline):
	model = models.Project
	extra = 5

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
	# list_display = ("username", "interaction")
	# search_fields = ["user__username"]
	list_display = ("username", "interaction", "_projects")
	search_fields = ["user__username"]

	inlines = [
		ProjectsInline
	]

	def _projects(self, obj):
		return obj.projects.all().count()