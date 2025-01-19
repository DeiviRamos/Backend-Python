import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["Espadas", "Diamante", "Corazones", "Trebol"]

def init_deck():
    deck = {}
    used_cards = set()
    
    while len(deck) < 2:
        card = random.choice(cards)
        suit = random.choice(suits)
        
        card_combo = (card, suit)
        
        if card_combo not in used_cards:
            used_cards.add(card_combo)
            deck[card] = suit
    
    return deck
            
deck_one = init_deck()
deck_second = init_deck()
print(deck_one)
print(deck_second)

def get_card(ask_hand):
    hand = ask_hand
    
    card = random.choice(cards)
    suit = random.choice(suits)
    
    hand[card] = suit
    
    return hand

deck_one = get_card(deck_one)
print(deck_one)

def calculate_points(hand):
    points = 0
    for card in hand:
        if card in {"J", "K", "Q"}:
            points+=10
        elif card == "A":
            points+=11 if points <= 10 else 1
        else:
            points+= int(card)
    return points


def results(first, second):
    point_first = calculate_points(first.keys())
    point_second = calculate_points(second.keys())
    
    if point_first > point_second and point_first <= 21:
        winner = "Jugador 1"
    elif point_first < point_second and point_second <= 21:
        winner = "Jugador 2"
    else: 
        winner = "Empate"
        
    return {"Jugador 1": point_first, "Jugador 2": point_second, "Ganador": winner}    

resultados = results(deck_one, deck_second)
print(resultados)
    

