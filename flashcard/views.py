from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Deck, Card
from .forms import DeckForm, CardForm

@login_required
def deck_list(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'flashcard/deck_list.html', {'decks': decks})

@login_required
def deck_detail(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    return render(request, 'flashcard/deck_detail.html', {'deck': deck})

@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_list')
    else:
        form = DeckForm()
    return render(request, 'flashcard/deck_form.html', {'form': form})

@login_required
def create_card(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.save()
            return redirect('deck_detail', deck_id=deck.id)
    else:
        form = CardForm()
    return render(request, 'flashcard/card_form.html', {'form': form, 'deck': deck})

@login_required
def delete_card(request, deck_id, card_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    card = get_object_or_404(Card, id=card_id, deck=deck)
    if request.method == 'POST':
        card.delete()
        return redirect('deck_detail', deck_id=deck.id)
    return render(request, 'flashcard/card_confirm_delete.html', {'card': card})

@login_required
def review_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    cards = deck.cards.all()
    return render(request, 'flashcard/review_deck.html', {'deck': deck, 'cards': cards})
