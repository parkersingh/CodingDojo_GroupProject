from django.db import models
import random
# Create your models here.
class Game(models.Model):
    num_decks = models.IntegerField()
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    user_cards=[]
    comp_cards=[]

    def shuffle(self,deck):
        random.shuffle(self.deck)
    def hit(self):
        card=self.deck.pop()
        self.user_cards.append(card)
    
    def user_sum(self):
        sum = 0
        for card in self.user_cards:
            if card == 'A':
                pass
            elif card == 'J' or card == 'Q' or card == 'K':
                sum += 10
            else:
                sum += card
        if 'A' in self.user_cards:
            if sum + 11 > 21:
                sum += 1
            else:
                sum += 11
        return sum
    
    def comp_sum(self):
        sum = 0
        for card in self.comp_cards:
            if card == 'A':
                pass
            elif card == 'J' or card == 'Q' or card == 'K':
                sum += 10
            else:
                sum += card
        if 'A' in self.comp_cards:
            if sum + 11 > 21:
                sum += 1
            else:
                sum += 11
        return sum

