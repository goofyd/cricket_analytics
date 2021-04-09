from django.contrib import admin
from .models import Tournament, Match, Team, MatchType, Venue, Player, Innings, Score

admin.site.register(MatchType)
admin.site.register(Venue)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Innings)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Score)