from django import forms
from .models import Vote, Player

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['voter_name', 'vote_3_points_player', 'vote_2_points_player', 'vote_1_point_player', 'fines']

    voter_name = forms.CharField(required=False)
    vote_3_points_player = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select Player for 3 Points",
        required=False
    )
    vote_2_points_player = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select Player for 2 Points",
        required=False
    )
    vote_1_point_player = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select Player for 1 Point",
        required=False
    )
    fines = forms.CharField(widget=forms.Textarea, required=False)
