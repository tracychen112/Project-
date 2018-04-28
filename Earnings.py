import datetime
import RegressionModel
import RBF 

now = datetime.datetime.now()

items = {0:[""]*10,1:[""]*10, 2:[""]*10, 3:[""]*10, 4:[""]*10, 5:[""]*10}

# money left to invest, earnings/losses, total account--unsure of this one?
def calculate(items):
    newLst = reorganizeLst(items)
    for lst in newLst:
        if lst[1]=='BUY':
            earnings = buy(lst)
    
    
    
    
    
'''
    year = date[2]
    if len(date[0])==1:
        month = '0'+date[0]
    else:
        month = date[0]
    if len(date[1])==1:
        day = '0'+date[1]
    else:
        day = date[1]
    endDate = year+'-'+month+'-'+day
'''
            

def buy(lst):
    try:
        data = quandl.get('WIKI/'+lst[0],start_date=date[0],end_date=date[1],column_index=4)
        dates = quandl.get('WIKI/'+lst[0],start_date=date[0],end_date=date[1],column_index=0)
        datelst = RegressionModel.getDates(dates)
        valLst = RegressionModel.getClosingValues(data)
        rbfval = RBF.mainPredict(datelst,valLst,predDays)
        linVal = RegressionModel.linearReg(datelst,valLst,predDays)
        price = (rbVal[1][-1]+linVal[-1])/2
        
        # calculate buy here 
        currPrice = valLst[-1]
        change =currPrice-price 
        shares = lst[2]
        result = shares*change
        return result
    except:
        pass 

def dateRange(date):
    now = datetime.datetime.now()
    currDate = str(now)
    day = int(now.day)
    year = int(now.year)
    month = int(now.month)
    # getting 15 days before for training
    pastDay = int(day)-15
    if pastDay<1: 
        pastDay-=31-pastDay
        month=int(month)-1
        if month<1:
            month =12-int(month)
            year= int(year)-1
    if len(str(month))==1:
        month = '0'+str(month)
    else:
        month = str(month)
    if len(str(pastDay))==1:
        pastDay = '0'+str(pastDay)
    else:
        pastDay = str(pastDay)
    startDate = str(year) + '-' +  month + '-' + pastDay
    return (startDate,currDate)

    

def reorganizeLst(items):
    itemlst = []
    for i in range(10):
        templst = []
        for index in range(6):
            templst.append(items[index][i])
        itemlst.append(templst)
    return itemlst
        
#print(calculate)