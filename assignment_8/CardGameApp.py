import tkinter as tk
from deck import Deck

class CardGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Game")
        self.deck = Deck()

        # Create a menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Create a File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Game", command=self.new_game)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

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
            comparison = self.compare_cards(self.player1_card, self.player2_card)
            if comparison > 0:
                self.result_label.config(text="Player 1 wins!")
            elif comparison < 0:
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
        rank_values = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
        }

        rank1_value = rank_values.get(card1.rank, 0)
        rank2_value = rank_values.get(card2.rank, 0)

        return rank1_value - rank2_value

    def new_game(self):
        self.deck = Deck()
        self.player1_card = None
        self.player2_card = None
        self.update_labels()
