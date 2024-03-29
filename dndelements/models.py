from django.db import models
from django.contrib.auth.models import User


class Bonus(models.Model):
    ability = models.CharField(max_length=40)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.ability


class ItemBonus(models.Model):
    ability = models.CharField(max_length=40)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.ability 

class Alignment(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class StatList(models.Model):
    charisma = models.IntegerField(default = 0)
    wisdom = models.IntegerField(default = 0)
    intelligence = models.IntegerField(default = 0)
    strength = models.IntegerField(default = 0)
    constitution = models.IntegerField(default = 0)
    dexterity = models.IntegerField(default = 0)

class Item(models.Model):
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=40)
    price = models.IntegerField(default = 0)
    effects = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    age = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    weight = models.IntegerField(default = 0)
    size = models.CharField(max_length=40)
    speed = models.IntegerField(default = 0)
    vision = models.CharField(max_length=40)
    languages = models.CharField(max_length=40)
    skill_boni = models.CharField(max_length=40)
    ability_boni = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class PlayerClass(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    origin = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="players")
    age = models.IntegerField(default = 0)
    level = models.IntegerField(default = 1)
    experience = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)
    player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE, related_name="players", null=True)
    player_stats = models.ForeignKey(StatList, on_delete=models.CASCADE, null=True)

    # can only be one owner ?? i dont understand this one to many many to one thing anymore
    # so every time you inser t aplayer, you have to pick 1 owner, but you can do 2 times a player with the same owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)

    running = models.BooleanField(default=False)
    rpg_variant = models.CharField(max_length=40, blank=True)

    players = models.ManyToManyField(Player, blank=True, related_name="campaigns")

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return self.name


class NPC(models.Model):
    name = models.CharField(max_length=40)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="npcs")
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default="Alive")
    alignment = models.ForeignKey(Alignment, null=True, on_delete=models.CASCADE, related_name="npcs")
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE, related_name="npcs")
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE, related_name="npcs")

    def __str__(self):
        return self.name

    
    # locations = models.IntegerField(default = 0)
    # npcs = models.IntegerField(default = 0)
    # items 

    # players = 
    # sessions