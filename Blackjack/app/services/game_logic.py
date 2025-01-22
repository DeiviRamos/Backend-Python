import random

# Baraja
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["Espadas", "Diamante", "Corazones", "Trebol"]

# Inicializa una mano
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

# Agrega una carta a la mano
def get_card(ask_hand):
    hand = ask_hand
    
    card = random.choice(cards)
    suit = random.choice(suits)
    
    hand[card] = suit
    
    return hand

# Calcula los puntos a una mano
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

# Determina el resultado de la partida
def results(first, second):
    point_first = calculate_points(first.keys())
    point_second = calculate_points(second.keys())
    
    if point_first > point_second and point_first <= 21:
        winner = "Jugador 1"
    elif point_first < point_second and point_second <= 21:
        winner = "Jugador 2"
    else: 
        winner = "Empate"
        
    return {"Ganador": winner}    

# Transforma el suits en su signo
def convert_hand_to_symbols(hand):
    suit_symbols = {"Espadas": "♠", "Corazones": "♥", "Diamante": "♦", "Trebol": "♣"}
    
    return {
        card: suit_symbols.get(suit, suit)
        for card, suit in hand.items()
    }

