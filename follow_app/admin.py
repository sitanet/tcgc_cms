from django.contrib import admin

from follow_app.models import Comment, Team_Lead, Member, TeamMember

# Register your models here.
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(Team_Lead)
admin.site.register(TeamMember)

