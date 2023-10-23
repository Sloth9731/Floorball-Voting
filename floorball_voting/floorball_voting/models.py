from django.db import models

class Game(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    score = models.CharField(max_length=255, null=True, blank=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    goal = models.TextField(max_length=255, null=True, blank=True)
    match_votes = models.TextField(max_length=255, null=True, blank=True)
    minuites = models.TextField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'floorball_voting'
    
    def __str__(self):
        return f"Game on {self.date} at {self.location} - {self.team} {self.score} Result: {self.result}"


class Vote(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=255, null=True, blank=True)
    vote_3_points = models.CharField(max_length=255)
    vote_2_points = models.CharField(max_length=255)
    vote_1_point = models.CharField(max_length=255)
    fines = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Vote by {self.voter_name} for Game on {self.game.date} against {self.game.team}"