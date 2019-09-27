# Generated by Django 2.2.5 on 2019-09-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndelements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='npc',
            name='status',
            field=models.CharField(default='Alive', max_length=40),
        ),
        migrations.AlterField(
            model_name='npc',
            name='campaign',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Campaign'),
        ),
    ]