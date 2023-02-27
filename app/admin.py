from django.contrib import admin
from .models import JobPost, Author, Location, Skill


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(JobPost, JobAdmin)
admin.site.register(Author)
admin.site.register(Location)
admin.site.register(Skill)