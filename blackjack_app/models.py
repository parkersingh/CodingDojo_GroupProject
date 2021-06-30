from django.db import models
import random
# Create your models here.
class Game(models.Model):
    num_decks = models.IntegerField()
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    user_cards=[]
    comp_cards=[]

    def shuffle(self,deck):
        self.deck = random.shuffle(deck)
        return
    def hit(self):
        card=self.deck.pop()
        self.user_cards.append(card)