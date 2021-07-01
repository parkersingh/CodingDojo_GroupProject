from django.shortcuts import render, HttpResponse, redirect
from .models import Blackjack


#Create your views here.
def index(request):
    return render(request, 'index.html')

def game(request):
    context={
        'last_game':Blackjack.objects.last()
    }
    return render(request, 'game.html', context)

def create(request):
    if request.method == 'POST':
        Blackjack.user_cards=[]
        Blackjack.comp_cards=[]
        new_game = Blackjack.objects.create(
            num_decks=request.POST['number']
        )
        
        new_game.deck = new_game.deck * 4 * int(request.POST['number'])
        new_game.shuffle(new_game.deck)
        first_card_user=new_game.deck.pop()
        second_card_user=new_game.deck.pop()
        first_card_comp=new_game.deck.pop()
        second_card_comp=new_game.deck.pop()
        new_game.user_cards.append(first_card_user)
        new_game.user_cards.append(second_card_user)
        new_game.comp_cards.append(first_card_comp)
        new_game.comp_cards.append(second_card_comp)
    return redirect('/game')

def hit(request):
    current_game = Blackjack.objects.last()
    sum=0
    for card in current_game.user_cards:
        if card == 'J'or card =='Q'or card =='K':
            sum+=10
        elif card == 'A':
            if sum > 10:
                sum+=1
            else:
                sum+=11
        else:
            sum+=card
    if sum < 21:
        current_game.hit()
    if sum > 21:
        return HttpResponse('Bust, CPU Wins!')
    return redirect('/game')

def stand(request):
    current_game=Blackjack.objects.last()
    if current_game.user_sum() > 21:
        return HttpResponse('CPU Won!')
    elif current_game.user_sum() > current_game.comp_sum():
        while current_game.user_sum() > current_game.comp_sum():
            current_game.comp_hit()
        if current_game.comp_sum() <=21:
            return HttpResponse('CPU Wins!')
        else:
            return HttpResponse('Player Wins!')
    return redirect('/game')