from tkinter import *
import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")

def getDates():
    # Dates 
    dates = quandl.get('WIKI/FB',rows = 5)
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
    closingVal  = quandl.get('WIKI/FB.4',rows = 5)

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
    increment = width/len(dates) 
    connectLines = []
    radius = 5 
    
    # temp 
    """
    for i in range(2):
        xPos = (i+1)*increment
        yPos = height-closingValues[i]
        connectLines.append((xPos,yPos))
    """
    canvas.create_rectangle(0,0,width,height,fill="white")
    for i in range(len(dates)):
        xPos = (i+1)*increment
        yPos = height-closingValues[i]
        connectLines.append((xPos,yPos))
        canvas.create_text(xPos,height-10,text=dates[i],font="Calibri 5 bold")
    
    yIncrement = height/20
    for i in range(20):
        yPos = i*yIncrement
        val = height-yPos
        canvas.create_text(20,yPos,text=str(val),font="Calibri 5 bold")
        
    
    
    canvas.create_line(connectLines,width=5)
    for point in connectLines:
        canvas.create_oval(point[0]-radius,point[1]-radius,point[0]+radius,point[1]+radius,fill="red")
    

def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("done!")

runDrawing(600, 500)





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


