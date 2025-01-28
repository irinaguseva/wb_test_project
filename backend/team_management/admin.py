from django.contrib import admin
from .models import Creator, Team, Member, TeamApplication


admin.site.register(Creator)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(TeamApplication)