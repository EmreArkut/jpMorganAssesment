from datetime import timedelta 
from datetime import datetime
import math

class Stock:
    def __init__(self, stockSymbol,stockType,lastDividend,fixedDividend, parValue ):
        '''
        Initialize Stock.
        
        '''
        self.stockSymbol =stockSymbol
        self.stockType = stockType       
        self.lastDividend = lastDividend
        self.fixedDividend =fixedDividend             
        self.parValue = parValue
        
    def getStockSymbol(self): 
        return self.stockSymbol
    
    def getLastDividend(self): 
        return self.lastDividend
   
    def calculateDividendYield(self,stockPrice):
        try:
            return self.lastDividend/stockPrice
        except ZeroDivisionError as err:
            print('Handling run-time error in calculateDividendYield :', err)               
    
    def calculateFixedDividendYield(self,stockPrice): 
        try:       
            return (self.fixedDividend *self.parValue)/stockPrice
        except ZeroDivisionError as err:
            print('Handling run-time error in calculateFixedDividendYield :', err)

            
    def calculatePriceEarningsRatio(self,stockPrice):
        try:        
            return stockPrice/self.lastDividend
        except ZeroDivisionError as err:
            print('Handling run-time error in calculatePriceEarningsRatio :', err)

         
class Trade:  
    def __init__(self): 
        '''
        Initialize Trade.
        
        '''        
        self.trades = []       
        
    def saveTrade(self,trade):        
         self.trades.append(trade) 
    
    '''
    Stock Price is calculated from trades. 
    Buy trade increases stock Price and sell trade decreases stock price            
    '''           
    def calculateStockPrice(self,stockSymbol,trade):
        try:
            totalQuantity=0
            totalTradePriceQuantity=0
            for value in trade.trades:            
                if (value[0]==stockSymbol):
                    totalTradePriceQuantity=totalTradePriceQuantity+ value[2]*value[3]
                    if(value[4]=='B'):                
                        totalQuantity=totalQuantity+value[2]
                    else:
                        totalQuantity=totalQuantity-value[2]
                        
            
            return  totalTradePriceQuantity/totalQuantity
        except ZeroDivisionError as err:
            print('Handling run-time error in calculateStockPrice :', err)  
    
    '''
    Calculates Stock Price in input minute range.
          
    '''         
    def calculateStockPriceInLastXMinute(self,stockSymbol,trade,minuteRange):
        try:
            totalQuantity=0
            totalTradePriceQuantity=0
                
            for value in trade.trades:            
                if (value[0]==stockSymbol):
                    dateTimeStart= datetime.now() - timedelta(minutes=minuteRange)
                    #date_object = datetime.strptime(value[1], '%Y-%m-%d %H:%M:%S')            
                    if (dateTimeStart  < value[1] and value[1] <datetime.now() ) :
                        totalTradePriceQuantity=totalTradePriceQuantity+ value[2]*value[3]
                        if(value[4]=='B'):                
                            totalQuantity=totalQuantity+value[2]
                        else:
                            totalQuantity=totalQuantity-value[2]
                        
            
            return  totalTradePriceQuantity/totalQuantity            
        except ZeroDivisionError as err:
            print('Handling run-time error in calculateStockPriceInLastXMinute :', err)
        
