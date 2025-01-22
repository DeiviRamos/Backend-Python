from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.game_logic import init_deck, results, get_card, calculate_points, convert_hand_to_symbols

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para las mano de los jugadores
class PlayerHand(BaseModel):
    player_hand: dict

class GameHands(PlayerHand):
    dealer_hand: dict
    

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Blackjack"}

@app.get("/start")
def start_game():
    player_hand = init_deck()
    dealer_hand = init_deck()

    # Convertir ambas manos a símbolos
    player_hand = convert_hand_to_symbols(player_hand)
    dealer_hand = convert_hand_to_symbols(dealer_hand)
    
    return {"player_hand": player_hand, "dealer_hand": dealer_hand}

@app.post("/hit")
def get_hit(player_hand: PlayerHand):
    hand_new = get_card(player_hand.player_hand)
    points = calculate_points(hand_new.keys())
    busted = points > 21
    hand_new_with_symbols = convert_hand_to_symbols(hand_new)
    return {"player_hand": hand_new_with_symbols, "busted": busted}

@app.post("/results")
def calculate_results(hands: GameHands):
    winner = results(hands.player_hand, hands.dealer_hand)
    player_points = calculate_points(hands.player_hand.keys())
    dealer_points = calculate_points(hands.dealer_hand.keys())
    return {"winner": winner, "player_points": player_points, "dealer_points": dealer_points} 
 