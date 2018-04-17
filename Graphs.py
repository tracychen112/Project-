from tkinter import *
import quandl
import RegressionModel 
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
    def __init__(self,company,width,height,num):
        self.company = company 
        self.width = width
        self.height = height 
        self.rows = num
        self.dates = quandl.get('WIKI/'+self.company,rows=num)
        self.close = quandl.get('WIKI/'+self.company,rows=num,column_index=4)
        self.displayDates = []
        self.solidCloseValues = []
        self.numOrigVal = 0
        self.numPredictedVal= 0
    
    # rows and number more to be predicted 
    def getDates(self):
        # Dates 
        dates = quandl.get('WIKI/'+self.company,rows=5)
        #print (dates)
        #print (dates)
        #print( type(dates.index)) # type panda 
        #print(len(dates.index))
        # stack overflow for syntax tolist 
        #print(dates.index.tolist())
        print(self.displayDates)
        print (len(dates.index.tolist()))
        for d in dates.index.tolist():
            date = str(d)
            #print(date[:10])
            self.displayDates.append((date[:10]))
        #print (self.displayDates)
        return self.displayDates 
    
    def addDates(self,predicted):
        for prediction in predicted:
            self.displayDates.append(prediction[0])
            print (self.displayDates)
    
    def getClosingValues(self):
        # Graphing closing values:
        # closing values 
        # Get numbers of a specific column 
        # CHECK CLOSING VALUES 
        # print(closingVal)
        for val in self.close:
            for i in range(len(self.close[val])):
                self.solidCloseValues.append(self.close[val][i])
                self.numOrigVal+=1
        return self.solidCloseValues
        #print(plotClosingVal)

    def predictedCloseValues(self,predicted):
        for prediction in predicted:
            self.solidCloseValues.append(prediction[1])
            self.numPredictedVal+=1
        

class Solid(Graph):
    
    def drawSolid(self,canvas):
        #print(closingValues)
        #print (closingValues)
        connectLines = []
        newLines = []
        radius = 5 
        margin = self.width/10
        increment = (self.width-2*margin)/len(self.displayDates)
        canvas.create_rectangle(0,0,self.width,self.height,fill="light blue",width=0)
        canvas.create_rectangle(margin,margin,self.width-margin,self.height-margin,fill="white")
        startY = self.height-margin
        startingPt = margin/2
        yBase = startY-startingPt
        minimum = int(min(self.solidCloseValues))
        # y-axis: values 
        #print(max(closingValues))
        #print(min(closingValues))
        yIncrement = (self.height-2*margin)/len(self.displayDates)
        #print (yIncrement)
        scale = (max(self.solidCloseValues)-min(self.solidCloseValues))/len(self.displayDates)
        scale = int(scale)+1
        #adjustPoints = yIncrement/scale * (closingValues[i]-minimum)
        for i in range(len(self.displayDates)):
            yPos = yBase-i*yIncrement
            val = minimum + i*scale
            canvas.create_line(7*margin/8,yPos,margin,yPos)
            canvas.create_text(7*margin/8,yPos,text=str(val),anchor= E,font="Calibri 10 bold")
    
        # x-axis: dates and addpoints 
        print('num predict',self.numPredictedVal)
        print('dates',self.solidCloseValues)
        for i in range(len(self.displayDates)):
            xPos = i*increment + margin + startingPt
            yPos = yBase-yIncrement/scale* (self.solidCloseValues[i]-minimum)
            if i==self.numOrigVal-1:
                newLines.append((xPos,yPos))
                connectLines.append((xPos,yPos))
            elif i>self.numOrigVal-1:
                newLines.append((xPos,yPos))
            else:
                connectLines.append((xPos,yPos))
            canvas.create_line(xPos,self.height-margin,xPos,self.height-7*margin/8)
            # stack overflow for angle 
            canvas.create_text(xPos,self.height-30,text=self.displayDates[i],font="Calibri 8 bold",angle=90) 
        
        # draw predicted  
        if len(newLines)>1:
            canvas.create_line(newLines,width=3,fill="purple")
            for i in range(len(newLines)):
                if i!=0:
                    point = newLines[i]
                    canvas.create_oval(point[0]-radius,point[1]-radius,point[0]+radius,point[1]+radius,fill="pink")
        
        # drawing past lines and points
        canvas.create_line(connectLines,width=3)
        for point in connectLines:
            canvas.create_oval(point[0]-radius,point[1]-radius,point[0]+radius,point[1]+radius,fill="red")
        
        
                
            
class CandleStick(Graph):
    def __init__(self,company,width,height,num):
        super().__init__(company,width,height,num)
        self.open = quandl.get('WIKI/'+self.company,column_index=1,rows=num)
        self.high = quandl.get('WIKI/'+self.company,column_index=2,rows=num)
        self.low = quandl.get('WIKI/'+self.company,column_index=3,rows=num)
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
        self.increment = (self.width-2*self.margin)/len(self.dates)
        
    def getScale(self):
        lowVal = []
        for val in self.low:
            for i in range(len(self.low[val])):
                lowVal.append(self.low[val][i])
        self.minVal = min(lowVal)
        self.minimum = int(self.minVal)
        highVal = []
        for val in self.high:
            for i in range(len(self.high[val])):
                highVal.append(self.high[val][i])
        self.maxVal = max(highVal)
        scale = (self.maxVal-self.minVal)/len(self.dates)
        self.scale = int(scale)+1
        print(self.maxVal,self.minVal,self.minimum)
        print('low',lowVal)
        print('high',highVal)
        print('scale',self.scale)
        
    def getLowValues(self):
        for val in self.low:
            for i in range(len(self.low[val])):
                value = self.low[val][i]
                newVal = self.yBase-self.yIncrement/self.scale*(value-self.minimum)
                self.convertLow.append(newVal)
        print('converted low',self.convertLow)
        
    def getHighValues(self):
        for val in self.high:
            for i in range(len(self.high[val])):
                value = self.high[val][i]
                newVal = self.yBase-self.yIncrement/self.scale*(value-self.minimum)
                self.convertHigh.append(newVal)
        
    def getOpenValues(self):
        for val in self.open:
            for i in range(len(self.open[val])):
                value = self.open[val][i]
                newVal = self.yBase-self.yIncrement/self.scale*(value-self.minimum)
                self.convertOpen.append(newVal)

    def getCloseValues(self):
        for val in self.close:
            for i in range(len(self.close[val])):
                value = self.close[val][i]
                newVal = self.yBase-self.yIncrement/self.scale*(value-self.minimum)
                self.convertClose.append(newVal)
        
    
    def drawCandleStick(self,canvas):
    
        canvas.create_rectangle(0,0,self.width,self.height,fill="light green",width=0)
        canvas.create_rectangle(self.margin,self.margin,self.width-self.margin,self.height-self.margin,fill="white")
        
        for i in range(len(self.dates)):
            xPos = i*self.increment + self.margin + self.startingPt
            # high and low plot
            # values are FLIPPED-higher-means low, lower means high 
            if self.convertClose[i]>self.convertOpen[i]:
                bottom = self.convertClose[i]
                top = self.convertOpen[i]
                color = 'red'
            else:
                bottom = self.convertOpen[i]
                top = self.convertClose[i]
                color = 'white'
            canvas.create_line(xPos,self.convertHigh[i],xPos,top)
            canvas.create_line(xPos,self.convertLow[i],xPos,bottom)
            canvas.create_rectangle(xPos-5,top,xPos+5,bottom,fill=color)
            # markers on x-axis 
            canvas.create_line(xPos,self.height-self.margin,xPos,self.height-7*self.margin/8)
            # stack overflow for angle 
            canvas.create_text(xPos,self.height-30,text=self.dates[i],font="Calibri 8 bold",angle=90) 
        
        for i in range(len(self.dates)):
            yPos = self.yBase-i*self.yIncrement
            val = self.minimum + i*self.scale
            canvas.create_line(7*self.margin/8,yPos,self.margin,yPos)
            canvas.create_text(7*self.margin/8,yPos,text=str(val),anchor= E,font="Calibri 10 bold")


## 112 website template 
def init(data):
    data.startState = True 
    data.drawCandle = False 
    data.drawSolidLine = False 
    data.width = 700
    data.height = 600 
    data.drawPredicted = False 
    pass 

def mousePressed(event, data):
    pass 

def redrawAll(canvas, data):
    if data.startState:
        Cover.draw(canvas,data.width,data.height)
    elif data.drawCandle:
        candle = CandleStick('FB',data.width,data.height,5)
        candle.getScale()
        candle.getLowValues()
        candle.getHighValues()
        candle.getOpenValues()
        candle.getCloseValues()
        candle.drawCandleStick(canvas)
    elif data.drawSolidLine:
        line = Solid('FB',data.width,data.height,5)
        line.getClosingValues()
        line.getDates()
        if data.drawPredicted:
            # two days for now 
            predictedVal = RegressionModel.linearReg(2,5)
            print (predictedVal)
            line.addDates(predictedVal)
            line.predictedCloseValues(predictedVal)
        line.drawSolid(canvas)
        
        

# press s for solid line graph
# press c for candlestick graph
# press b to go back to original state
# press p to predict  
def keyPressed(event, data):
    if event.keysym=="c":
        data.drawCandle= True 
        data.startState = False
        data.drawSolidLine = False
    elif event.keysym=="s":
        data.drawCandle= False 
        data.startState = False
        data.drawSolidLine = True 
    elif event.keysym=="b":
        data.drawCandle= False
        data.startState = True 
        data.drawSolidLine = False
    elif event.keysym=="p":
        data.drawPredicted = not data.drawPredicted 
        

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
