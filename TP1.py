from tkinter import *
import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")


company = input("Enter stock symbol of a company: ")

class Graph(object):
    def __init__(self,company):
        self.company = company 
        self.dates = quandl.get('WIKI/'+company,rows=5)
        


class Solid(Graph):
                
            
class CandleStick(Graph):
    def __init__(self):
        super().__init__(self)
        self.open = quandl.get('WIKI/'+self.company,column_index=1)
        self.high = quandl.get('WIKI/'+self.company,column_index=2)
        self.low = quandl.get('WIKI/'+self.company,column_index=3)
        # may delete this for inheritance 
        self.close = quandl.get('WIKI/'+self.company,column_index=4)
        
    def getLowValues(self):
        lowVal = []
        for val in self.low:
            for i in range(len(self.low[val])):
                lowVal.append((self.low[val][i]))
        return lowVal 
        
    def getHighValues(self):
        highVal = []
        for val in self.high:
            for i in range(len(self.high[val])):
                highVal.append((self.high[val][i]))
        return highVal
    
        
    def getOpenValues(self):
        openVal = []
        for val in self.open:
            for i in range(len(self.open[val])):
                openVal.append((self.open[val][i]))
        return lowVal
    
    # from inheritance may delete this later 
    def getClosingValues(self):
        closeVal = []
        for val in self.close:
            for i in range(len(self.close[val])):
                openVal.append((self.close[val][i]))
        return closeVal
    
    def draw(self,canvas):
        
        
            
        
    
    
"""
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
        canvas.create_line(7*margin/8,yPos,margin,yPos)
        canvas.create_text(7*margin/8,yPos,text=str(val),anchor= E,font="Calibri 10 bold")

    
    # x-axis: dates and addpoints 
    for i in range(len(dates)):
        xPos = i*increment + margin + startingPt
        yPos = yBase-yIncrement/scale* (closingValues[i]-minimum)
        connectLines.append((xPos,yPos))
        canvas.create_line(xPos,height-margin,xPos,height-7*margin/8)
        # stack overflow for angle 
        canvas.create_text(xPos,height-30,text=dates[i],font="Calibri 8 bold",angle=90)    
    # drawing out lines
    canvas.create_line(connectLines,width=3)
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

"""

## 112 website template 
def init(data):
    self.startState = True 
    self.drawCandle = False 
    self.drawSolidLine = False 
    pass 

def mousePressed(event, data):
    pass 

def redrawAll(canvas, data):
    pass 

def keyPressed(event, data):
    pass

def timerFired(data):
    pass 

####################################
# use the run function as-is   
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
runDrawing(700, 600)
