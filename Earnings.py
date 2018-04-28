items = {0:[""]*10,1:[""]*10, 2:[""]*10, 3:[""]*10, 4:[""]*10, 5:[""]*10}

# money left to invest, earnings/losses, total account--unsure of this one?
def calculate(items):
    newLst = reorganizeLst(items)
    for lst in newLst:
        if lst[1]=='BUY':
            earnings = buy(lst)
            
            

def buy(lst):
    
    try:
        quandl.get('WIKI/'+lst[0],
    

def dateRange(date):
    date = lst[3].split("/")
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
    return (startDate,endDate)
    
    

def reorganizeLst(items):
    itemlst = []
    for i in range(10):
        templst = []
        for index in range(6):
            templst.append(items[index][i])
        itemlst.append(templst)
    return itemlst
        
#print(calculate)