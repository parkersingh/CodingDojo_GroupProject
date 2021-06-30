from django.db import models
import math, random

from django.db.models.expressions import Value
# Create your models here.

# Card class to store info of each individual playing card
class Blackjack(models.Model):
    num_decks = models.IntegerField()
    deck = []
    player_hand = []
    cpu_hand = []

    def create_deck(self):
        new_deck = []
        for num in range(0, self.num_decks):
            for val in range(1, 14):
                for count in range(0, 4):
                    if val == 1:
                        new_deck.append('A')
                    elif val == 11:
                        new_deck.append('J')
                    elif val == 12:
                        new_deck.append('Q')
                    elif val == 13:
                        new_deck.append('K')
                    else:
                        new_deck.append(val)
        random.shuffle(new_deck)
        return new_deck
    
    def add_player_hand(self):
        self.player_hand.append(self.deck.pop(0))
        return self
    
    def add_player_hand(self):
        self.player_hand.append(self.deck.pop(0))
        return self
    
    def player_total(self):
        total = 0
        for card in self.player_hand:
            if card == 'A':
                pass
            elif card == 'J' or card == 'Q' or card == 'K':
                total += 10
            else:
                total += card
        if 'A' in self.player_hand:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total
    
    def cpu_total(self):
        total = 0
        for card in self.cpu_hand:
            if card == 'A':
                pass
            elif card == 'J' or card == 'Q' or card == 'K':
                total += 10
            else:
                total += card
        if 'A' in self.cpu_hand:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total


    


