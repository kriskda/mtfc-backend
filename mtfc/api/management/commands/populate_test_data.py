from django.core.management.base import BaseCommand
from api.models import Group, Team, Player, Match, Set
from random import randint


TEAM_NUM_PER_GROUP = 3
PLAYER_NUM_PER_TEAM = 2

GROUP_NAMES = ['Group A', 'Group B', 'Group C', 'Group D']
TEAM_NAMES = ['Team ' + str(i + 1) for i in range(0, len(GROUP_NAMES) * TEAM_NUM_PER_GROUP)]
PLAYER_NAMES = [['Name' + str(i), 'Surname' + str(i)] for i in range(0, len(TEAM_NAMES) * PLAYER_NUM_PER_TEAM)]
FAKE_EMAIL = 'test@test.pl'


class Command(BaseCommand):
    args = ''
    help = 'Populates db with fake data'

    def _create_groups(self):
        map(lambda x: Group(name=x).save(), GROUP_NAMES)

    def _create_teams(self):
        groups = Group.objects.all()

        for i, group in enumerate(groups):
            start = i * TEAM_NUM_PER_GROUP
            end = (i + 1) * TEAM_NUM_PER_GROUP

            map(lambda x: Team(name=x, group=group).save(), TEAM_NAMES[start:end])

    def _create_players(self):
        teams = Team.objects.all()

        for i, team in enumerate(teams):
            start = i * PLAYER_NUM_PER_TEAM
            end = (i + 1) * PLAYER_NUM_PER_TEAM

            map(lambda x: Player(first_name=x[0], last_name=x[1], email=FAKE_EMAIL, team=team).save(),
                PLAYER_NAMES[start:end])

    def _create_matches(self):
        # Generating first match
        team_a = Team.objects.get(pk=1)
        team_b = Team.objects.get(pk=2)

        match = Match(team_a=team_a, team_b=team_b)
        match.save()

        for i in range(0, 3):
            goals_a = randint(0, 5)
            goals_b = randint(0, 5) if goals_a == 5 else 5

            Set(match=match, goals_a=goals_a, goals_b=goals_b).save()

        # Generating second match...DRY sucks here ;-)
        team_a = Team.objects.get(pk=3)
        team_b = Team.objects.get(pk=4)

        match = Match(team_a=team_a, team_b=team_b)
        match.save()

        for i in range(0, 3):
            goals_a = randint(0, 5)
            goals_b = randint(0, 5) if goals_a == 5 else 5

            Set(match=match, goals_a=goals_a, goals_b=goals_b).save()

    def handle(self, *args, **options):
        self._create_groups()
        self._create_teams()
        self._create_players()
        self._create_matches()