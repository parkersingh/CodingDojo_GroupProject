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

# Check_sum of player's cards after a new card is dealt
def check_sum(reqeust):
    game = Blackjack.objects.last()
    player_sum = game.player_sum()
    if player_sum() > 21:
        return HttpResponse('Bust')
    else:
        return HttpResponse('Return back to game')

def cpu_hit(request):
    game = Blackjack.objects.last()
    cpu_sum = game.cpu_sum()
    if cpu_sum > 21:
        return HttpResponse('Cpu Bust')
    elif cpu_sum <= 21 and cpu_sum >= 17:
        return redirect('Check Results')
    else:
        game.add_cpu_hand()
        return HttpResponse('Back to cpu turn')

def check_results(request):
    game = Blackjack.objects.last()
    player_total = game.player_sum()
    cpu_total = game.cpu_sum()
    if player_total > cpu_total:
        return HttpResponse('Player Wins')
    elif player_total == cpu_total:
        return HttpResponse('Tie')
    else:
        return HttpResponse('Cpu Wins')
