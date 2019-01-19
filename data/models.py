from game import game
from player import player
from django.db import models
from django import forms

# Create your models here.
class Data(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

class Transliterate(models.Model):
    text = models.TextField()
    choices = (('0','UK IPA'), ('1','US IPA'), ('2','Klattese'), ('3','SAMPA'), ('4','ARPABET'))
    src = models.CharField(max_length = 2, choices = choices)
    dst = models.CharField(max_length = 2, choices = choices)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]

class Random(models.Model):
    nouns = models.SlugField(blank = True)
    verbs = models.SlugField(blank = True)
    adj = models.SlugField(blank = True)
    prep = models.SlugField(blank = True)
    verbs_i = models.SlugField(blank = True)
    adv = models.SlugField(blank = True)

    def __str__(self):
        return self.title

class Game(models.Model):
    player1 = models.SlugField(blank = True)
    player2 = models.SlugField(blank = True)
    p1Score = models.SlugField(blank = True)
    p2Score = models.SlugField(blank = True)
    gameId = models.SlugField(blank = True)
    isFull = models.SlugField(blank = True)

class Player(models.Model):
    playerName = models.SlugField(blank = True)
    
