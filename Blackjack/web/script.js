let playerHand = {};
let dealerHand = {};

// Referencia a los contenedores de cartas
const playerCardsContainer = document.getElementById("player-cards");
const dealerCardsContainer = document.getElementById("dealer-cards");

// Renderizar cartas gráficas
function renderCards(container, hand) {
  container.innerHTML = ""; // Limpiar las cartas previas
  Object.entries(hand).forEach(([value, suit]) => {
    const card = document.createElement("div");
    card.classList.add("card");
    if (suit === "♥" || suit === "♦") {
      card.classList.add("red");
    }

    // Crear las partes de la carta
    const header = document.createElement("div");
    header.classList.add("card-header");
    header.textContent = value;

    const suitSymbol = document.createElement("div");
    suitSymbol.classList.add("card-suit");
    suitSymbol.textContent = suit;

    const footer = document.createElement("div");
    footer.classList.add("card-footer");
    footer.textContent = value;

    card.appendChild(header);
    card.appendChild(suitSymbol);
    card.appendChild(footer);
    container.appendChild(card);
  });
}


// Botón: Iniciar juego
document.getElementById("btn-deal").addEventListener("click", () => {
  fetch("http://127.0.0.1:8000/start")
    .then((response) => response.json())
    .then((data) => {
      playerHand = data.player_hand;
      dealerHand = data.dealer_hand;

      // Renderizar las cartas gráficas
      renderCards(playerCardsContainer, playerHand);
      renderCards(dealerCardsContainer, dealerHand);

      document.getElementById("btn-hit").disabled = false;
      document.getElementById("btn-stand").disabled = false;
      document.getElementById("message").textContent = "";
    })
    .catch((error) => {
      console.error("Error al iniciar el juego:", error);
    });
});


// Botón: Pedir carta (Hit)
document.getElementById("btn-hit").addEventListener("click", () => {
  fetch("http://127.0.0.1:8000/hit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ player_hand: playerHand }),
  })
    .then((response) => response.json())
    .then((data) => {
      playerHand = data.player_hand;

      // Renderizar las cartas actualizadas
      renderCards(playerCardsContainer, playerHand);

      if (data.busted) {
        document.getElementById("message").textContent =
          "Te pasaste de 21. ¡Has perdido!";
        document.getElementById("btn-hit").disabled = true;
        document.getElementById("btn-stand").disabled = true;
      }
    })
    .catch((error) => {
      console.error("Error al pedir carta:", error);
    });
});


  
// Boton para resultados
  document.getElementById("btn-stand").addEventListener("click", () => {
    fetch("http://127.0.0.1:8000/results", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ player_hand: playerHand, dealer_hand: dealerHand }),
    })
      .then((response) => response.json())
      .then((data) => {
        const { winner, player_points, dealer_points } = data;
        document.getElementById("message").textContent = `
          Ganador: ${winner} 
          (Jugador: ${player_points} puntos, Dealer: ${dealer_points} puntos)
        `;
        document.getElementById("btn-hit").disabled = true;
        document.getElementById("btn-stand").disabled = true;
      })
      .catch((error) => {
        console.error("Error al finalizar el turno:", error);
      });
  });
  