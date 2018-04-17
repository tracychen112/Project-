import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
# Simple linear regression 

# calculate current data set- find which one errs the least- then use that one to calculate the future 

# predict prices in a certain amount of days in the future 
#days = input("number of days in the future: ")


# From graphics 
def getDates(num):
    # Dates 
    dates = quandl.get('WIKI/FB',limit= num)
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

def getClosingValues(num):
    # Graphing closing values:
    # closing values 
    # Get numbers of a specific column 
    closeVal = []
    prices = quandl.get('WIKI/FB',limit=num,column_index= 4)
    # CHECK CLOSING VALUES 
    # print(closingVal)
    for val in prices:
        for i in range(len(prices[val])):
            closeVal.append(prices[val][i])
    return closeVal 


def linearReg(days,pastDays):
    # X
    dates = getDates(pastDays)
    future = getDates(pastDays+days)
    print (future)
    print (dates)
    m = len(dates)
    print (m)
    indVar = list(range(1,m+1))
    # Y CLOSING PRICES AKA dependent variable
    prices = getClosingValues(pastDays)
    xHat = sum(indVar)/len(indVar)
    yHat = sum(prices)/len(prices)
    numerator = 0
    denominator = 0 
    
    #  format taken from https://mubaris.com/2017/09/28/linear-regression-from-scratch/
    for i in range(0,m):
        numerator+=((indVar[i]-xHat)*(prices[i]-yHat))
        denominator+=((indVar[i]-xHat)**2)

    b1 = numerator/denominator
    b0 = yHat-(b1*xHat)
    
    projected = list(range(m+1,m+1+int(days)))
    print (projected)
    projectedCoord = []
    for day in projected:
        predictedPrice = b0+ b1*day
        projectedCoord.append((future[day-1],predictedPrice))
        print("Day " + str(day) + ": ",predictedPrice)
    return projectedCoord
     

# also from https://mubaris.com/2017/09/28/linear-regression-from-scratch/
# lower RMSE values indicate better fit 
# there will be predicted set of past data and actual past data
def rootMeanSquareError(predicted,actual):
    m = len(predicted)
    difference = 0 
    for day in predicted:
        difference+=(predicted[0]-actual[0])**2
    rmse = math.sqrt(difference/m)
    return rmse 


      
# vector regression
# w*x + b>=theta -one class, otherwise belongs to another class, w and x are vectors of d dimension  
#  w*x dot product summation 

#   do dot product here
# f(x) = <w,x> + b with w E X, b E R
# minimize w  

#https://pythonprogramming.net/svm-in-python-machine-learning-tutorial/
class SVM(object):
    def __init__(self):
        pass 
    
    # f(x) = <w,x> + b    
    def predict(self,features):
        w = self.w
        # dot product of w and features
        dotProduct = w[0]*features[0] + w[1]*features[1]
        number = dotProduct + self.b 
        if number<0:
            classifcation = -1
        elif number>0:
            classification = 1
        else:
            classification = 0 
        return classification 

print ('hi')