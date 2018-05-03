import RegressionModel
import RBF 
import quandl 
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'

# calculations of strategy/Portfolio page 

def calculate(items):
    errorPresent = False 
    newLst = reorganizeLst(items)
    overallEarn = 0
    index =0 
    count=0
    countError = 0
    for lst in newLst:
        if lst[0]!="" and lst[2]!="":
            try:
                recentPrice = quandl.get('WIKI/'+lst[0],rows=1,column_index=4)
            except:
                countError+=1
                pass 
            for d in recentPrice:
                recentPrice = list(recentPrice[d]) 
            items[3][index] = '%0.2f' % recentPrice[0] 
            items[4][index] = '%0.2f' % (recentPrice[0]*int(items[2][index]))  
        
        earnings,futPrice,errorPresent = move(lst)
        if errorPresent:
            countError+=1
        if earnings!=None and futPrice!=None:
            items[6][index]= "%0.2f" % futPrice
            items[7][index]= "%0.2f" % earnings
            overallEarn+=earnings 
            print('overallEarn', overallEarn)
        else:
            count+=1
        index+=1
    if count==10:
        earnings = ''
        errorPresent = False  
    elif countError>1:
        errorPresent = True
        if overallEarn>0:
            earnings = '%0.2d' % (overallEarn)
        else:
            earnings  = 0
    elif overallEarn==0:
        earnings='0'
        errorPresent = False 
    else:
        earnings = '%0.2d' % (overallEarn)
        errorPresent = False 
    print('count error',countError)
    print('earnings',earnings)
    return (items,earnings,errorPresent)
    
    
    
months = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

def move(lst):
    count = 0
    for n in lst:
        if n=='':
            count+=1
    if count==len(lst):
        return (None,None,False)
    try:
        futureDate = lst[5].split('/')
        print  ('future Date', futureDate)
        if len(futureDate)>3:
            return (None,None,True)
        else:
            gapYear = int(futureDate[2])-2018
            gapMonth = int(futureDate[0])-3        
            if gapYear<0 or gapMonth<0:
                return (None,None,True)
            else:
                gapDay = int(futureDate[1])-27
                if gapDay<0 and gapMonth>0:
                    gapDay = months[futureDate[0]]-27 + int(futureDate[1])
                elif gapDay<0 and gapMonth<=0:
                    return (None,None,True)
        predDays = gapYear*365 + gapMonth*31 + gapDay 
    except:
        (None,None,True)
    start = '2018-01-01'
    try:
        data = quandl.get('WIKI/'+lst[0],start_date=start,end_date='2018-03-27',column_index=4)
        dates = quandl.get('WIKI/'+lst[0],start_date=start,end_date='2018-03-27')

        datelst = RegressionModel.getDates(dates)
        valLst = RegressionModel.getClosingValues(data)
        rbf = RBF.mainPredict(datelst,valLst,predDays)
        
        linVal = RegressionModel.linearReg(datelst,valLst,predDays)
        price = (rbf[1][-1]+linVal[-1])/2
        
        lastVal = quandl.get('WIKI/'+lst[0],rows=1)
        # calculate here
        currPrice = valLst[-1]
        change =(price-currPrice) 
        shares = int(lst[2])
        result = shares*change
        if lst[1]=='SHORT':
            result=-result
        elif lst[1]!='BUY':
            result = None  
            return (result,price,True)
        return (result,price,False)
    except:
        return (None,None,True)

    

def reorganizeLst(items):
    itemlst = []
    for i in range(10):
        templst = []
        for index in range(6):
            templst.append(items[index][i])
        itemlst.append(templst)
    return itemlst
        
