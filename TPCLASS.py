from tkinter import *
import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")




class Cover(object):
    
    def __init__(self,width,height):
        self.width = width
        self.height = height 
    
    @staticmethod
    def draw(canvas,width,height):
        canvas.create_rectangle(0,0,width,height,fill="light pink")
        pass 
        
    

class Graph(object):
    def __init__(self,company,width,height):
        self.company = company 
        self.width = width
        self.height = height 
        self.dates = quandl.get('WIKI/'+self.company,rows=5)
        self.close = quandl.get('WIKI/'+self.company,rows=5,column_index=4)
    
    def getDates(self):
        # Dates 
        dates = quandl.get('WIKI/'+self.company,rows = 5)
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

    def getClosingValues(self):
        # Graphing closing values:
        # closing values 
        # Get numbers of a specific column 
        closeVal = []
        # CHECK CLOSING VALUES 
        # print(closingVal)
        for val in self.close:
            for i in range(len(self.close[val])):
                closeVal.append(self.close[val][i])
        print (closeVal)
        return closeVal 
    
        #print(plotClosingVal)

class Solid(Graph):
    
    def drawSolid(self,canvas):
        closingValues = self.getClosingValues()
        #print(closingValues)
        #print (closingValues)
        dates = self.getDates()
        connectLines = []
        radius = 5 
        margin = self.width/10
        increment = (self.width-2*margin)/len(dates)
        canvas.create_rectangle(0,0,self.width,self.height,fill="light blue")
        canvas.create_rectangle(margin,margin,self.width-margin,self.height-margin,fill="white")
    
        startY = self.height-margin
        startingPt = margin/2
        yBase = startY-startingPt
        minimum = int(min(closingValues))
        # y-axis: values 
        #print(max(closingValues))
        #print(min(closingValues))
        yIncrement = (self.height-2*margin)/len(dates)
        #print (yIncrement)
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
            canvas.create_line(xPos,self.height-margin,xPos,self.height-7*margin/8)
            # stack overflow for angle 
            canvas.create_text(xPos,self.height-30,text=dates[i],font="Calibri 8 bold",angle=90)    
        # drawing out lines
        canvas.create_line(connectLines,width=3)
        # draw points 
        for point in connectLines:
            canvas.create_oval(point[0]-radius,point[1]-radius,point[0]+radius,point[1]+radius,fill="red")
                
            
class CandleStick(Graph):
    def __init__(self,company,width,height):
        super().__init__(company,width,height)
        self.open = quandl.get('WIKI/'+self.company,column_index=1)
        self.high = quandl.get('WIKI/'+self.company,column_index=2)
        self.low = quandl.get('WIKI/'+self.company,column_index=3)
        self.convertOpen = []
        self.convertHigh = []
        self.convertLow = []
        self.convertClose = []
        self.margin = self.width/10
        self.startY = self.height-self.margin
        self.startingPt = self.margin/2
        self.yBase = self.startY-self.startingPt
        self.minimum = None 
        self.dates = self.getDates()
        self.yIncrement = (self.height-2*self.margin)/len(self.dates)
        # to get range:
        self.minVal = 0
        self.maxVal = 0 
        scale = (self.maxVal-self.minVal)/len(self.dates)
        self.scale = int(scale)+1
        
    def getLowValues(self):
        lowVal = []
        for val in self.low:
            for i in range(len(self.low[val])):
                lowVal.append(self.low[val][i])
        self.minVal = min(lowVal)
        self.minimum = int(self.minVal)
        for val in self.low:
            for i in range(len(self.low[val])):
                value = self.low[val][i]
                newVal = self.yIncrement/self.scale * (value-self.minimum)
                self.convertLow.append(newVal)
        
    def getHighValues(self):
        highVal = []
        for val in self.high:
            for i in range(len(self.high[val])):
                highVal.append(self.high[val][i])
        self.maxVal = max(highVal)
        for val in self.high:
            for i in range(len(self.high[val])):
                value = self.high[val][i]
                newVal = self.yIncrement/self.scale * (value-self.minimum)
                self.convertHigh.append(newVal)
        
    def getOpenValues(self):
        print ('c')
        for val in self.open:
            for i in range(len(self.open[val])):
                value = self.open[val][i]
                newVal = self.yIncrement/self.scale * (value-self.minimum)
                self.convertOpen.append(newVal)

    def getCloseValues(self):
        print ('d')
        for val in self.open:
            for i in range(len(self.open[val])):
                value = self.high[val][i]
                newVal = self.yIncrement/self.scale * (value-self.minimum)
                self.convertHigh.append(newVal)
        
    
    def drawCandleStick(self,canvas):
        print('hi')
        
        for i in range(len(dates)):
            xPos = i*self.increment + self.margin + self.startingPt
            # high and low plot 
            if self.convertClose[i]>self.convertOpen[i]:
                bottom = self.convertClose[i]
                top = self.convertOpen[i]
            else:
                bottom = self.convertOpen[i]
                top = self.convertClose[i]
            canvas.create_line(xPos,self.convertHigh[i],xPos,top)
            canvas.create_line(xPos,self.convertLow[i],xPos,bottom)
            canvas.create_line(xPos,self.height-margin,xPos,self.height-7*margin/8)
            # stack overflow for angle 
            canvas.create_text(xPos,self.height-30,text=dates[i],font="Calibri 8 bold",angle=90) 
        
        
            
        
    
    
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
    data.startState = True 
    data.drawCandle = False 
    data.drawSolidLine = False 
    data.width = 700
    data.height = 600 
    pass 

def mousePressed(event, data):
    pass 

def redrawAll(canvas, data):
    if data.startState:
        Cover.draw(canvas,data.width,data.height)
    elif data.drawCandle:
        candle = CandleStick('FB',data.width,data.height)
        candle.getLowValues()
        candle.getHighValues()
        candle.getOpenValues()
        candle.getCloseValues()
        candle.drawCandleStick(canvas)
    elif data.drawSolidLine:
        line = Solid('FB',data.width,data.height)
        line.drawSolid(canvas)
        

def keyPressed(event, data):
    if event.keysym=="c":
        data.drawCandle= True 
        data.startState = False
        data.drawSolidLine = False
    elif event.keysym=="s":
        data.candleStick= False 
        data.startState = False
        data.drawSolidLine = True 
    elif event.keysym=="b":
        data.candleStick= False
        data.startState = True 
        data.drawSolidLine = False

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

run(700, 600)
