# Reference
# https://sbcode.net/python/chain_of_responsibility/#chain_of_responsibilitychain_of_responsibility_conceptpy

import random

class BotUtils():
    def getBet(low,high):
        bet = random.randint(low, high)
        return bet
    
    def getNewBetAmount(lastBetAmount, bet, balance):
        newLastBet = lastBetAmount + bet
        if newLastBet >= balance:
            newLastBet = balance
        return newLastBet
            
    def checkNewBalance(balance, bet):
        newBalance = balance - bet
        if newBalance <= 0:
            newBalance = 0
        return newBalance
        
