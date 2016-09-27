from Stock import *
from datetime import timedelta 
from datetime import datetime

def test_calculateStockPrice():
    tradeTemp = Trade()
    emptyTradeList=[]
    tradeTemp.calculateStockPrice('AAA',emptyTradeList)
    
def test_calculateDividendYield():
    """
    Unit test for calculateDividendYield    
    """
    stockTemp=Stock('JOE','Common',2,0,100)
    calculateDividendYield(stockTemp,0)

    
def test_calculateFixedDividendYield():
    """
    Unit test for calculateFixedDividendYield  
    """
    # test 1


def test_calculatePriceEarningRatio():
    """
    Unit test for calculatePriceEarningRatio
    
    """

    
print "----------------------------------------------------------------------"
print "Initialize stocks"
stock1=Stock('JOE','Common',2,0,100) 
stock2=Stock('GIN','Preferred',8,0.02,100)
trade = Trade()
#Trades for stock1. Some of the trades in last 15 minutes
trade.saveTrade([stock1.getStockSymbol(),datetime.now() - timedelta(minutes=23),1000,23,'B'])
trade.saveTrade([stock1.getStockSymbol(),datetime.now() - timedelta(minutes=10),7000,11,'B'])
trade.saveTrade([stock1.getStockSymbol(),datetime.now() - timedelta(minutes=4),1000,45,'B'])
trade.saveTrade([stock1.getStockSymbol(),datetime.now() - timedelta(minutes=45),1000,12,'S'])
trade.saveTrade([stock1.getStockSymbol(),datetime.now() - timedelta(minutes=5),100000,23,'B'])
                    
#Transactions for stock2 Some of the trades in last 15 minutes
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=4),50000,23,'B'])
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=2),7000,11,'B'])
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=22),1000,45,'B'])
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=45),1000,12,'S'])
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=11),7000,23,'B'])
trade.saveTrade([stock2.getStockSymbol(),datetime.now() - timedelta(minutes=3),700,23,'S'])

print "----------------------------------------------------------------------"
print "Testing calculateStockPrice..."

trade.calculateStockPrice(stock1.getStockSymbol(),trade)
trade.calculateStockPrice(stock2.getStockSymbol(),trade)
print "Testing calculateDividendYield..."
stock1.calculateDividendYield( trade.calculateStockPrice(stock1.getStockSymbol(),trade))
print "----------------------------------------------------------------------"
print "Testing calculateFixedDividendYield..."
stock2.calculateFixedDividendYield(trade.calculateStockPrice(stock2.getStockSymbol(),trade))
print "----------------------------------------------------------------------"
print "Testing calculatePriceEarningsRatio..."
stock1.calculatePriceEarningsRatio(trade.calculateStockPrice(stock1.getStockSymbol(),trade))
stock2.calculatePriceEarningsRatio(trade.calculateStockPrice(stock2.getStockSymbol(),trade))
print "----------------------------------------------------------------------"
print "Testing calculateStockPriceInLastXMinute..."
trade.calculateStockPriceInLastXMinute('JOE',trade,15)
trade.calculateStockPriceInLastXMinute('GIN',trade,15)

print "All done!"

print "----------------------------------------------------------------------"
print "Testing calculateStockPrice..."        
test_calculateStockPrice()