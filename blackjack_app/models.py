from django.db import models
import math, random

from django.db.models.expressions import Value
# Create your models here.

class DeckManager(models.Manager):
# Check to see if deck is full

    # Create new deck based off number of decks given
    def create_deck(self, num_decks):
        for num in range(0, num_decks):
            for val in range(1, 11):
                for count in range(0, 4):
                    new_card = Card.objects.create(face= f'{val}', value= val)
                    self.cards_in_deck.append(new_card)
                if val == 10:
                    for suit in 'KQJ':
                        for i in range(0, 4):
                            face_card = Card.objects.create(face= f'{suit}', value= val)
                            self.cards_in_deck.append(face_card)

        random.shuffle(self.cards_in_deck)
        
        return self
    
    def full_deck(card_counter, num_decks):
        num_cards = 0
        for x in card_counter.values():
            num_cards += x
        return num_cards <= 52*num_decks
    
# Card class to store info of each individual playing card
class Card(models.Model):
    # CARD_SUITS = (('D', 'Diamond'),
    # ('C', 'Clubs'),
    # ('H,', 'Hearts'),
    # ('S', 'Spades'))
    # suit = models.CharField(max_length= 1, choices= CARD_SUITS)

    face = models.CharField(max_length= 10)
    value = models.IntegerField()

# Player class to handle the cards a user and the computer has
class Player(models.Model):
    cards_in_hand = []
    name = models.CharField(max_length= 50)

#Create and shuffle cards needed for a game depending on the number of decks used
class Deck(models.Model):
    num_decks = models.IntegerField()
    cards_in_deck = []
    objects = DeckManager()