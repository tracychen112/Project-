# Simple linear regression 



# predict prices in a certain amount of days in the future 
days = input("number of days in the future: ")

# From graphics 
def getDates():
    # Dates 
    dates = quandl.get('WIKI/FB',rows = 5)
    #print (dates)
    #print( type(dates.index)) # type panda 
    #print(len(dates.index))
    # stack overflow for syntax tolist 
    #print(dates.index.tolist())
    datesLst = []
    for d in dates.index.tolist():
        #print(d)
        date = str(d)
        datesLst.append((date[:10]))
    return datesLst

def getClosingValues():
    # Graphing closing values:
    # closing values 
    # Get numbers of a specific column 
    closeVal = []
    prices = quandl.get('WIKI/FB',rows=5,column_index= 4)
    # CHECK CLOSING VALUES 
    # print(closingVal)
    for val in self.close:
        for i in range(len(self.close[val])):
            closeVal.append(self.close[val][i])


def linearReg():
    # X
    dates = getDates()
    m = len(dates)
    indVar = list(range(1,m+1))
    # Y CLOSING PRICES AKA dep variable
    prices = getClosingValues()
    xHat = sum(indVar)/len(indVar)
    yHat = sum(prices)/len(prices)
    
    for i in range(0,m):
        numerator+=((indVar[i]-xHat)*(prices[i]-yHat))
        denominator+=((indVar[i]-xHat)**2)
    
    b1 = numerator/denominator
    b0 = yHat-(b1*xHat)
    
    projected = list(range(m+1,m+1+days))
    projectedCoord = []
    for day in projected:
        predictedPrice = b0+ b1*day
        projectedCoord.append((day,predictedPrice))
        
    
    
      
    
 
