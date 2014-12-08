from api.models import *
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'email')


# Fix that!
# TODO: Team should not accept more than two players
def validate_player_number(self):
    if self.players.queryset.count > 2:
        raise serializers.ValidationError('Team already has 2 players')


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True, validators=[validate_player_number])

    class Meta:
        model = Team
        fields = ('id', 'name', 'group', 'players')


class GroupSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'teams')


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('match', 'goals_a', 'goals_b')


class MatchSerializer(serializers.ModelSerializer):
    team_a = TeamSerializer(read_only=True)
    team_b = TeamSerializer(read_only=True)
    sets = SetSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'played_date', 'team_a', 'team_b', 'sets')
