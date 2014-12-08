# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('played_date', models.DateField(default=datetime.date(2014, 12, 8))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=100)),
                ('last_name', models.CharField(default=b'', max_length=100)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
                'ordering': ('last_name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goals_a', models.PositiveSmallIntegerField(default=0)),
                ('goals_b', models.PositiveSmallIntegerField(default=0)),
                ('match', models.ForeignKey(related_name='sets', to='api.Match')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('group', models.ForeignKey(related_name='teams', to='api.Group')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(related_name='players', to='api.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='team_a',
            field=models.OneToOneField(related_name='match_team_a', to='api.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='team_b',
            field=models.OneToOneField(related_name='match_team_b', to='api.Team'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('team_a', 'team_b')]),
        ),
    ]
