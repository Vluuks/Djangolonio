from django.db import models


# class Bonus(models.Model):
#     ability = models.CharField(max_length=40)
#     score = models.IntegerField(default = 0)

# class ItemBonus(models.Model):
#     ability = models.CharField(max_length=40)
#     score = models.IntegerField(default = 0)


# class Item(models.Model):
#     description = models.CharField(max_length=1000)
#     name = models.CharField(max_length=40)
#     price = models.IntegerField(default = 0)
#     boni = 

# class Race(models.Model):
#     description = models.CharField(max_length=1000)
#     name = models.CharField(max_length=40)
#     age = models.IntegerField(default = 0)
#     height = models.IntegerField(default = 0)
#     weight = models.IntegerField(default = 0)
#     size = models.CharField(max_length=40)
#     speed = models.IntegerField(default = 0)
#     vision = models.CharField(max_length=40)
#     languages = models.CharField(max_length=40)
#     skill_boni = models.CharField(max_length=40)
#     ability_boni = models.CharField(max_length=40)


class Player(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="races")
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)

    # can only be one owner ?? i dont understand this one to many many to one thing anymore
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="campaigns")


class NPC(models.Model):
    name = models.CharField(max_length=40)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="races")
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)


class Campaign(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=40)
    
    # locations = models.IntegerField(default = 0)
    # npcs = models.IntegerField(default = 0)
    # items 

    # players = 
    # sessions