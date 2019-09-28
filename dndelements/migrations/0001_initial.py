# Generated by Django 2.2.5 on 2019-09-28 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('running', models.BooleanField(default=False)),
                ('rpg_variant', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('origin', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('age', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=40)),
                ('speed', models.IntegerField(default=0)),
                ('vision', models.CharField(max_length=40)),
                ('languages', models.CharField(max_length=40)),
                ('skill_boni', models.CharField(max_length=40)),
                ('ability_boni', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('age', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('experience', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=40)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL)),
                ('player_class', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='dndelements.PlayerClass')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='dndelements.Race')),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=40)),
                ('status', models.CharField(default='Alive', max_length=40)),
                ('campaign', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Campaign')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Race')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='campaigns', to='dndelements.Player'),
        ),
    ]
