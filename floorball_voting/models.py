from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    match_votes = models.IntegerField(default=0)
    team_votes = models.IntegerField(default=0)
    penalties = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    score = models.CharField(max_length=255, null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    goal = models.TextField(max_length=255, null=True, blank=True)
    assists = models.TextField(max_length=255, null=True, blank=True)
    match_votes = models.TextField(max_length=255, null=True, blank=True)
    minuites = models.TextField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'floorball_voting'
    
    def __str__(self):
        return f"Game on {self.date} at {self.location} - {self.team} {self.score} Result: {self.result}"


class Vote(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=255, null=True, blank=True)

    # Each vote instance has three player fields for different point levels
    vote_3_points_player = models.ForeignKey(Player, related_name='votes_3_points', on_delete=models.SET_NULL, null=True, blank=True)
    vote_2_points_player = models.ForeignKey(Player, related_name='votes_2_points', on_delete=models.SET_NULL, null=True, blank=True)
    vote_1_point_player = models.ForeignKey(Player, related_name='votes_1_point', on_delete=models.SET_NULL, null=True, blank=True)

    fines = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Vote by {self.voter_name} for game on {self.game.date} against {self.game.team}"
