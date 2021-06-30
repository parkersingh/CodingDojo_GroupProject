from django.shortcuts import render, HttpResponse, redirect
from .models import Blackjack

# Create your views here.
def index(request):
    return render(request, 'index.html')

def start_game(request):
    # new_game = Blackjack.objects.create(num_decks= request.POST['num_decks'])
    new_game = Blackjack.objects.first()
    new_game.deck = new_game.create_deck()
    for i in range(0, 2):
        new_game.add_player_hand()
        new_game.add_cpu_hand()
    
    return HttpResponse(f'Deck Cards: {len(new_game.deck)}, Player Cards: {new_game.player_hand}, Cpu Cards: {new_game.cpu_hand}')