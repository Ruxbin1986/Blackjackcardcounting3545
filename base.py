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


# Create a deck instance
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Display the shuffled deck
deck.display()