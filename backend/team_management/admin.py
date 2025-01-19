from django.contrib import admin

# Register your models here.
# python manage.py makemigrations team_management
# python manage.py migrate

from .models import Creator, Team, Member, TeamApplication

admin.site.register(Creator)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(TeamApplication)