from django.contrib import admin
from .models import Links,Skills,Profile,Jobroles,Projects
# Register your models here.
admin.site.register(Profile)
admin.site.register(Jobroles)
admin.site.register(Links)

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['name','option']
admin.site.register(Skills,SkillsAdmin)

admin.site.register(Projects)

