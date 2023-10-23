from django import forms
from .models import Vote, Game

PLAYER_CHOICES = [(player, player) for player in [
    'Adam Biddle', 'Alex Sket', 'Asher Bartulovich', 'Daniel Steffanoni', 'Finn Hay', 'Flynn Craig', 'Harry Fahrner', 'James Hollingsworth', 
    'Kiran Kulcar', 'Sam Weight', 'Sarah Guilfoyle', 'Stephan Samuel' , 'Thomas Gambuti', 'William Charles', 'Zoe Shanahan'
]]

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [ 'voter_name', 'vote_3_points', 'vote_2_points', 'vote_1_point', 'fines']

    voter_name = forms.CharField(required=False)
    vote_3_points = forms.ChoiceField(choices=[('', 'Select Player for 3 Points')] + PLAYER_CHOICES)
    vote_2_points = forms.ChoiceField(choices=[('', 'Select Player for 2 Points')] + PLAYER_CHOICES)
    vote_1_point = forms.ChoiceField(choices=[('', 'Select Player for 1 Point')] + PLAYER_CHOICES)
    fines = forms.CharField(widget=forms.Textarea, required=False)
