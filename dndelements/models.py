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
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="players"")
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)

    # can only be one owner ?? i dont understand this one to many many to one thing anymore
    # so every time you inser t aplayer, you have to pick 1 owner, but you can do 2 times a player with the same owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="players")


class NPC(models.Model):
    name = models.CharField(max_length=40)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="npcs")
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="npcs")


class Campaign(models.Model):
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=40)
    users = models.ManyToMany(User, blank=True, related_name="campaigns")
    
    # locations = models.IntegerField(default = 0)
    # npcs = models.IntegerField(default = 0)
    # items 

    # players = 
    # sessions