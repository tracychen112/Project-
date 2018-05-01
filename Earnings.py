import RegressionModel
import RBF 
import quandl 
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'


# money left to invest, earnings/losses, total account--unsure of this one?
def calculate(items,day,month,year):
    newLst = reorganizeLst(items)
    print('here',newLst)
   # print ('hi',newLst)
    overallEarn = 0
    print('list',newLst)
    index =0 
    count=0
    for lst in newLst:
        #print (lst)
        #print('result',move(lst))
        if lst[0]!="" and lst[2]!="":
            recentPrice = quandl.get('WIKI/'+lst[0],rows=1,column_index=4)
            for d in recentPrice:
                recentPrice = list(recentPrice[d]) 
            items[3][index] = '%0.2f' % recentPrice[0] 
            items[4][index] = '%0.2f' % (recentPrice[0]*int(items[2][index]))  
        
        earnings,futPrice = move(lst,day,month,year)
        if earnings!=None and futPrice!=None:
            items[6][index]= "%0.2f" % futPrice
            items[7][index]= "%0.2f" % earnings
            overallEarn+=earnings 
        else:
            count+=1
        index+=1
    if count==10:
        earnings = ''
    elif overallEarn==0:
        earnings='0'
    else:
        earnings = '%0.2d' % (overallEarn)
    return (items,earnings)
    
    
    
    
    
    
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
            

def move(lst,day,month,year):
    #print('date predetermined',Graphs.Portfolio.month,Graphs.Portfolio.day,Graphs.Portfolio.year)
    if len(day)==1:
        day = '0'+day
    if len(month)==1:
        month = '0'+month
    start = year+'-'+month+'-'+day 
    try:
        #print('comp',lst[0])
        data = quandl.get('WIKI/'+lst[0],start_date=start,end_date='2018-03-27',column_index=4)
        dates = quandl.get('WIKI/'+lst[0],start_date=start,end_date='2018-03-27')
        #print(data)
        #print ('company',lst[0])
        #print ('start',date[0])
        #print('end', date[1])
        #print ('date: ',dates)
        #dates2 = RegressionModel.getDates(dates)
        datelst = RegressionModel.getDates(dates)
        valLst = RegressionModel.getClosingValues(data)
        predDays = 10
        rbf = RBF.mainPredict(datelst,valLst,predDays)
        #print('here',rbfVal)
        linVal = RegressionModel.linearReg(datelst,valLst,predDays)
        price = (rbf[1][-1]+linVal[-1])/2
        
        lastVal = quandl.get('WIKI/'+lst[0],rows=1)
        # calculate buy here 
        currPrice = valLst[-1]
        change =(currPrice-price) 
        shares = int(lst[2])
        result = shares*change
        if lst[1]=='SHORT':
            result=-result
        return (result,price)
    except:
        return (None,None)

"""
def dateRange():
    now = Graph.endDate 
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
"""
    

def reorganizeLst(items):
    itemlst = []
    for i in range(10):
        templst = []
        for index in range(6):
            templst.append(items[index][i])
        itemlst.append(templst)
    #print(itemlst)
    return itemlst
        
#print(calculate)