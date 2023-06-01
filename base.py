import random

class Deck:
    """Represents a deck of playing cards."""

    def __init__(self):
        """Initialize a standard deck of 52 cards."""
        self.cards = []
        self._build_deck()

    def _build_deck(self):
        """Build a standard deck of 52 cards."""
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def display(self):
        """Display the cards in the deck."""
        for card in self.cards:
            print(card)

class Card:
    """Represents a playing card."""

    def __init__(self, suit, rank):
        """Initialize a card with the given suit and rank."""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a string representation of the card."""
        return f"{self.rank} of {self.suit}"

class Hand:
    """Represents a player's or dealer's hand of cards in blackjack."""

    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand."""
        self.cards.append(card)

    def get_value(self):
        """Calculate the value of the hand."""
        value = 0
        num_aces = 0

        for card in self.cards:
            value += card.get_value()

            # Keep track of the number of aces in the hand
            if card.rank == 'A':
                num_aces += 1

        # Adjust the value for aces
        while value > 21 and num_aces > 0:
            value -= 10  # Treat an ace as 1 instead of 11
            num_aces -= 1

        return value

    def display(self):
        """Display the cards in the hand."""
        for card in self.cards:
            print(card)

class Dealer:
    """Represents the dealer in a game of blackjack."""

    def __init__(self):
        """Initialize the dealer's attributes."""
        self.hand = Hand()
        self.is_dealer_turn = False

    def show_initial_card(self):
        """Show the dealer's initial card (face-up)."""
        print("Dealer's initial card:")
        print(self.hand.cards[0])

    def play_turn(self, deck):
        """Play the dealer's turn based on the game rules."""
        self.is_dealer_turn = True

        while self.hand.get_value() < 17:
            self.hit(deck)

    def hit(self, deck):
        """Dealer takes a card from the deck and adds it to their hand."""
        card = deck.deal_card()
        self.hand.add_card(card)

    def display_hand(self):
        """Display the dealer's hand."""
        print("Dealer's hand:")
        self.hand.display()

    def reset(self):
        """Reset the dealer's attributes for a new round."""
        self.hand = Hand()
        self.is_dealer_turn = False

class Player:
    """Represents a player in a game of blackjack."""

    def __init__(self, name):
        """Initialize the player's attributes."""
        self.name = name
        self.hand = Hand()
        self.is_busted = False

    def hit(self, deck):
        """Player takes a card from the deck and adds it to their hand."""
        card = deck.deal_card()
        self.hand.add_card(card)
        print(f"{self.name} hits and receives: {card}")

        if self.hand.get_value() > 21:
            self.is_busted = True

    def stand(self):
        """Player chooses to stand (not take additional cards)."""
        print(f"{self.name} stands.")

    def display_hand(self):
        """Display the player's hand."""
        print(f"{self.name}'s hand:")
        self.hand.display()

    def reset(self):
        """Reset the player's attributes for a new round."""
        self.hand = Hand()
        self.is_busted = False

class Game:
    """Represents a game of blackjack."""

    def __init__(self):
        """Initialize the game attributes."""
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Dealer()

    def start(self):
        """Start the game."""
        print("Welcome to Blackjack!")
        self.deck.shuffle()
        self.deal_initial_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.play_again()

    def deal_initial_cards(self):
        """Deal the initial cards to the player and dealer."""
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.show_initial_card()

    def player_turn(self):
        """Handle the player's turn."""
        while not self.player.is_busted:
            choice = input("Do you want to hit or stand? (h/s): ")
            if choice.lower() == 'h':
                self.player.hit(self.deck)
                self.player.display_hand()
            else:
                self.player.stand()
                break

    def dealer_turn(self):
        """Handle the dealer's turn."""
        self.dealer.display_hand()
        if self.player.is_busted:
            return

        self.dealer.play_turn(self.deck)
        self.dealer.display_hand()

    def display_result(self):
        """Display the game result."""
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        print("----- Results -----")
        print("Player's hand:", player_value)
        print("Dealer's hand:", dealer_value)

        if self.player.is_busted:
            print("Player busts! Dealer wins.")
        elif self.dealer.is_busted:
            print("Dealer busts! Player wins.")
        elif player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")