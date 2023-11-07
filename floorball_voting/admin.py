from django.contrib import admin
from .models import Vote, Game, Player

class GameAdmin(admin.ModelAdmin):
    list_display = ('date', 'location')

admin.site.register(Vote)
admin.site.register(Game, GameAdmin)
admin.site.register(Player)
