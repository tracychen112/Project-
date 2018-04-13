from tkinter import *
import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")



def getClosingValues():
    # Graphing closing values:

    # closing values 
    closingVal  = quandl.get('WIKI/FB.4',rows = 5)


    dataHigh = quandl.get('WIKI/FB.2',rows = 5) 

    dataLow = quandl.get('WIKI/FB.3',rows = 5)
    #print(data.index)

    # Get numbers of a specific column 

    plotClosingVal = []
    print(closingVal)
    for val in closingVal:
        for i in range(len(closingVal[val])):
            plotClosingVal.append((closingVal[val][i]))
    return plotClosingVal 
    #print(plotClosingVal)


# 112 website template 
def draw(canvas, width, height):
    closingValues = getClosingValues()
    increment = width/5 
    connectLines = []
    radius = 5 
    
    # temp 
    """
    for i in range(2):
        xPos = (i+1)*increment
        yPos = height-closingValues[i]
        connectLines.append((xPos,yPos))
    """
    for i in range(5):
        xPos = (i+1)*increment
        yPos = height-closingValues[i]
        connectLines.append((xPos,yPos))
    
    print (connectLines)
    
    canvas.create_rectangle(0,0,width,height,fill="white")
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

runDrawing(400, 200)





#### MORE QUANDL FEATURES BELOW 


#print(data)
#data2 = quandl.get('WIKI/AAPL',limit=1,column_index=3)    # this will get 1949 records
#print(data2)
#print(data.head(5))
#print(data.tail(5))
#print(data.count())


#data = quandl.get("WIKI/TSLA", start_date="2018-03-20", end_date="2018-04-10")
#print(data.head(5))
#print(data.tail(5))

""" KNOW HOW TO BULK DOWNLOAD??
#quandl.bulkdownload(data)
"""


