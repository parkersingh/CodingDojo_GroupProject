from django.shortcuts import render, HttpResponse, redirect
from .models import Game


#Create your views here.
def index(request):
    context={
        'last_game':Game.objects.last()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        new_game = Game.objects.create(
            num_decks=request.POST['number']
        )
        print(new_game.deck)
        print(int(request.POST['number']))
        new_game.deck = new_game.deck * 4 * int(request.POST['number'])
        print(new_game.deck)
        new_game.shuffle(new_game.deck)
        
        print(new_game.deck)
        print(new_game.deck)

        first_card_user=new_game.deck.pop()
        second_card_user=new_game.deck.pop()
        first_card_comp=new_game.deck.pop()
        second_card_comp=new_game.deck.pop()
        new_game.user_cards.append(first_card_user)
        new_game.user_cards.append(second_card_user)
        new_game.comp_cards.append(first_card_comp)
        new_game.comp_cards.append(second_card_comp)
    return redirect('/')
