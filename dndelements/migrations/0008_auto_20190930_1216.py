# Generated by Django 2.2.5 on 2019-09-30 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndelements', '0007_auto_20190929_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='npc',
            name='alignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npcs', to='dndelements.Alignment'),
        ),
    ]
