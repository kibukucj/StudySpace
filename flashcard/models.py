from django.contrib.auth.models import User
from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='decks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Card(models.Model):
    deck = models.ForeignKey(Deck, related_name='cards', on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('date_added',)