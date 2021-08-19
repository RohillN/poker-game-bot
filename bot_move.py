# Reference
# https://sbcode.net/python/chain_of_responsibility/#chain_of_responsibilitychain_of_responsibility_conceptpy

import random
from abc import ABCMeta, abstractmethod
from bot_utils import BotUtils

# Handler Interface Successors implement"
class IHandler(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def handle(roomId, botType, amountToBet, lastBetAmount, roundNumber, cardLength):
        "implemented method"
    
# Bluffer process
class Bluffer(IHandler):
    "A Concrete Handler"
    @staticmethod
    def handle(roomId, botType, balance, lastBetAmount, roundNumber, cardLength):
        print(f"Bluffer payload = {botType} : RoomID: {roomId} : {balance} : LastBetAmoun: {lastBetAmount}")
        chance = random.randint(0, 100)
        if chance >= 70 and chance <= 100:                                          # 30% chance to raise
            betLimit = BotUtils.getBet(5, 10)                                        # bet from 5 - 10
            newBetAmount = BotUtils.getNewBetAmount(lastBetAmount, betLimit, balance)
            newBalance = BotUtils.checkNewBalance(balance, betLimit)
            move = {"move": "BET", "betAmount": newBetAmount, "balance": newBalance}
        if chance >= 10 and chance <= 69 and lastBetAmount >= 0:                     # 60% chance to keep calling (if pot keeps going higher)
            newBalance = BotUtils.checkNewBalance(balance, lastBetAmount)
            move = {"move": "CALL", "betAmount": lastBetAmount, "balance": newBalance}
        if chance >= 0 and chance <= 9 or balance <= 0:                                             # 10% chance to fold
            move = {"move": "FOLD", "betAmount": 0, "balance": balance}
        if roundNumber == 2 or cardLength == 0:
            move = {"move": "SKIP", "betAmount": 0, "balance": 0}
        return move

# Riskers process
class Risker(IHandler):
    "A Concrete Handler"
    @staticmethod
    def handle(roomId, botType, balance, lastBetAmount, roundNumber, cardLength):
        print(f"Risker payload = {botType} : RoomID: {roomId} : {balance} : LastBetAmoun: {lastBetAmount}")
        chance = random.randint(0, 100)
        if chance >= 85 and chance <= 100:                                      # 15% chance to raise (higher raise)
            betLimit = BotUtils.getBet(5, 40)                                    # bet from 5 - 40
            newBetAmount = BotUtils.getNewBetAmount(lastBetAmount, betLimit, balance)
            newBalance = BotUtils.checkNewBalance(balance, betLimit)
            move = {"move": "BET", "betAmount": newBetAmount, "balance": newBalance}
        if chance >= 15 and chance <= 84 and lastBetAmount >= 0:                 # 70% chance to keep calling (if pot keeps going higher)
            newBalance = BotUtils.checkNewBalance(balance, lastBetAmount)
            move = {"move": "CALL", "betAmount": lastBetAmount, "balance": newBalance}
        if chance >= 0 and chance <= 14 or balance <= 0:                                        # 15% chance to fold
            move = {"move": "FOLD", "betAmount": 0, "balance": balance}
        if roundNumber == 2 or cardLength == 0:
            move = {"move": "SKIP", "betAmount": 0, "balance": 0}
        return move

# Conservative process
class Conservative(IHandler):
    "A Concrete Handler"
    @staticmethod
    def handle(roomId, botType, balance, lastBetAmount, roundNumber, cardLength):
        print(f"Conservative payload = {botType} : RoomID: {roomId} : {balance} : LastBetAmoun: {lastBetAmount}")
        chance = random.randint(0, 100)
        if chance >= 85 and chance <= 100:                                      # 15% chance to raise (higher raise)
            betLimit = BotUtils.getBet(5, 30)                                    # bet from 5 - 30
            newBetAmount = BotUtils.getNewBetAmount(lastBetAmount, betLimit, balance)
            newBalance = BotUtils.checkNewBalance(balance, betLimit) 
            move = {"move": "BET", "betAmount": newBetAmount, "balance": newBalance}
        if chance >= 40 and chance <= 84 and lastBetAmount >= 0:                 # 45% chance to keep calling (if pot keeps going higher)
            newBalance = BotUtils.checkNewBalance(balance, lastBetAmount)
            move = {"move": "CALL", "betAmount": lastBetAmount, "balance": newBalance}
        if chance >= 0 and chance <= 39 or balance <= 0:                                        # 40% chance to fold
            move = {"move": "FOLD", "betAmount": 0, "balance": balance}
        if roundNumber == 2 or cardLength == 0:
            move = {"move": "SKIP", "betAmount": 0, "balance": 0}
        return move

