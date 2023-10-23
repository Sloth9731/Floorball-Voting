# Generated by Django 4.2.4 on 2023-10-22 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(blank=True, max_length=255, null=True)),
                ('player_name', models.CharField(max_length=255)),
                ('vote_3_points', models.CharField(max_length=255)),
                ('vote_2_points', models.CharField(max_length=255)),
                ('vote_1_point', models.CharField(max_length=255)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('fines', models.TextField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floorball_voting.game')),
            ],
        ),
    ]
