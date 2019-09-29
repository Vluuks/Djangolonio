# Generated by Django 2.2.5 on 2019-09-29 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndelements', '0006_auto_20190928_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Campaign'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('campaign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='dndelements.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='npc',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Location'),
        ),
    ]
