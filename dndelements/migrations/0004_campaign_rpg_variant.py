# Generated by Django 2.2.5 on 2019-09-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndelements', '0003_remove_campaign_rpg_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='rpg_variant',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]