from game import Game
from game_blackjack import Game_Blackjack

g = Game()
g.test()
g.__class__ = Game_Blackjack
g.test()
