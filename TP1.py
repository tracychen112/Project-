from tkinter import *
import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")

try:
    # actually correct this part 
    company = input("Enter stock symbol of a company: ")
except: 
    print("ENTER VALID STOCK SYMBOL!")

def getDates():
    # Dates 
    dates = quandl.get('WIKI/'+company,rows = 5)
    #print (dates)
    print( type(dates.index)) # type panda 
    print(len(dates.index))
    # stack overflow for syntax tolist 
    print(dates.index.tolist())
    
    datesLst = []
    for d in dates.index.tolist():
        #print(d)
        date = str(d)
        datesLst.append((date[:10]))
    return datesLst


def getClosingValues():
    # Graphing closing values:

    # closing values 
    closingVal  = quandl.get('WIKI/'+company,rows = 5,column_index=4)

    dataHigh = quandl.get('WIKI/FB.2',rows = 5) 

    dataLow = quandl.get('WIKI/FB.3',rows = 5)
    # Get numbers of a specific column 

    plotClosingVal = []
    # CHECK CLOSING VALUES 
   # print(closingVal)
    for val in closingVal:
        for i in range(len(closingVal[val])):
            plotClosingVal.append((closingVal[val][i]))
    return plotClosingVal 
    #print(plotClosingVal)


# 112 website template 
def draw(canvas, width, height):
    closingValues = getClosingValues()
    print (closingValues)
    dates = getDates()
    connectLines = []
    radius = 5 
    margin = width/10
    increment = (width-2*margin)/len(dates)
    canvas.create_rectangle(0,0,width,height,fill="light blue")
    canvas.create_rectangle(margin,margin,width-margin,height-margin,fill="white")
    
    
    startY = height-margin
    startingPt = margin/2
    yBase = startY-startingPt
    minimum = int(min(closingValues))
    # y-axis: values 
    print(max(closingValues))
    print(min(closingValues))
    yIncrement = (height-2*margin)/len(dates)
    print (yIncrement)
    scale = (max(closingValues)-min(closingValues))/len(dates)
    scale = int(scale)+1
    #adjustPoints = yIncrement/scale * (closingValues[i]-minimum)
    for i in range(len(dates)):
        yPos = yBase-i*yIncrement
        val = minimum + i*scale
        canvas.create_text(20,yPos,text=str(val),font="Calibri 5 bold")

    
    # x-axis: dates and addpoints 
    for i in range(len(dates)):
        xPos = i*increment + margin + startingPt
        yPos = yBase-yIncrement/scale* (closingValues[i]-minimum)
        connectLines.append((xPos,yPos))
        canvas.create_text(xPos,height-30,text=dates[i],font="Calibri 5 bold")    
    # drawing out lines
    canvas.create_line(connectLines,width=5)
    # draw points 
    for point in connectLines:
        canvas.create_oval(point[0]-radius,point[1]-radius,point[0]+radius,point[1]+radius,fill="red")
    

def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("done!")

runDrawing(700, 600)





#### MORE QUANDL FEATURES BELOW 


#print(data)
#data = quandl.get('WIKI/AAPL',limit=1,column_index=3)    # this will get 1949 records
#print(data2)
#print(data.head(5))
#print(data.tail(5))
#print(data.count())
#print(data.index)

#data = quandl.get("WIKI/TSLA", start_date="2018-03-20", end_date="2018-04-10")
#print(data.head(5))
#print(data.tail(5))

""" KNOW HOW TO BULK DOWNLOAD??
#quandl.bulkdownload(data)
"""


