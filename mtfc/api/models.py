from datetime import date
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)


class Team(models.Model):
    group = models.ForeignKey(Group, related_name='teams')

    name = models.CharField(max_length=100, blank=False, default='')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)


class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players')

    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name',)


class Match(models.Model):
    team_a = models.OneToOneField(Team, related_name='match_team_a')
    team_b = models.OneToOneField(Team, related_name='match_team_b')

    played_date = models.DateField(default=date.today())

    class Meta:
        unique_together = ('team_a', 'team_b')


class Set(models.Model):
    match = models.ForeignKey(Match, related_name='sets')

    goals_a = models.PositiveSmallIntegerField(blank=False, default=0)
    goals_b = models.PositiveSmallIntegerField(blank=False, default=0)






