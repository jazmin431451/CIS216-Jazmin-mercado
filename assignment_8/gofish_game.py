import tkinter as tk
import random
import tkinter as tk
from deck import Deck
from card import Card

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop(0)
        return None

class CardGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Game")

        self.deck = Deck()

        self.player1_label = tk.Label(root, text="Player 1")
        self.player1_label.pack()

        self.player1_button = tk.Button(root, text="Draw", command=self.player1_draw)
        self.player1_button.pack()

        self.player2_label = tk.Label(root, text="Player 2")
        self.player2_label.pack()

        self.player2_button = tk.Button(root, text="Draw", command=self.player2_draw)
        self.player2_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.player1_card = None
        self.player2_card = None

    def player1_draw(self):
        self.player1_card = self.deck.draw()
        self.update_labels()

    def player2_draw(self):
        self.player2_card = self.deck.draw()
        self.update_labels()

    def update_labels(self):
        if self.player1_card and self.player2_card:
            if self.compare_cards(self.player1_card, self.player2_card) > 0:
                self.result_label.config(text="Player 1 wins!")
            elif self.compare_cards(self.player1_card, self.player2_card) < 0:
                self.result_label.config(text="Player 2 wins!")
            else:
                self.result_label.config(text="It's a tie!")
        else:
            self.result_label.config(text="")

        if self.player1_card:
            self.player1_label.config(text=str(self.player1_card))
        if self.player2_card:
            self.player2_label.config(text=str(self.player2_card))

    def compare_cards(self, card1, card2):
        # Implement your card comparison logic here
        return 0  # Default to a tie

if __name__ == "__main__":
    root = tk.Tk()
    app = CardGameApp(root)
    root.mainloop()
