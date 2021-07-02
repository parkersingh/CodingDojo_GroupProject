from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Blackjack
from datetime import datetime, date


#Create your views here.
def index(request):
    return render(request, 'index.html')

def tutorial(request):
    return render(request, 'tutorial.html')

def age_check(request):
    return render(request, 'age_check.html')

def validate_age(request):
    today = date.today()
    user_dob = datetime.strptime(request.POST['age'], '%Y-%m-%d')
    age = today.year - user_dob.year - ((today.month, today.day) < (user_dob.month, user_dob.year))
    if age >= 18:
        return redirect('/index')
    else:
        error = 'Age entered is not 18 or over'
        messages.error(request, error)
        return redirect('/')

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
    if current_game.user_sum() > 21:
        error = 'You busted. CPU Wins!'
        messages.error(request, error)
    return redirect('/game')

def stand(request):
    current_game = Blackjack.objects.last()
    if current_game.user_sum() > 21:
        error = 'You busted. CPU Wins!'
        messages.error(request, error)
    else:
        while current_game.comp_sum() < 17:
            current_game.comp_hit()
        if current_game.user_sum() < current_game.comp_sum() and current_game.comp_sum() <= 21:
            error = 'CPU Wins!'
            messages.error(request, error)
        elif current_game.user_sum() == current_game.comp_sum():
            error = 'Tie!'
            messages.error(request, error)
        else:
            error = 'Player Wins!'
            messages.error(request, error)
    return redirect('/game')