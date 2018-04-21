from tkinter import *  
import string 
import quandl
import RegressionModel 
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#data <- Quandl.datatable('MER/F1', compnumber="39102")


class Cover(object):

    @staticmethod
    def draw(canvas,width,height):
        canvas.create_rectangle(0,0,width,height,fill="lavender",width=0)
        canvas.create_text(width/2,height/3,text="iStockUp",font="Dubai 50",fill="black")
        # Dubai, Gigi
        
class Choice(object):
    @staticmethod
    def draw(canvas,width,height):
        canvas.create_rectangle(0,0,width,height,fill="light yellow",width=0)
        canvas.create_text(width/2,height/10,text="Options",font="Dubai 50",fill="black")
        # View graphs 
        canvas.create_rectangle(width/8,3*height/8,4*width/9,7*height/8,fill="white")
        # View earnings/portfolio 
        canvas.create_text(103*width/144,2*height/7,text="My Earnings",font="Dubai 35",fill="black")
        canvas.create_rectangle(5*width/9,3*height/8,7*width/8,7*height/8,fill="white")
        # canvas.create_image(103*width/144,5*height/8,image="piggyBank.jpg")
        # text for graphs 
        canvas.create_text(41*width/144,2*height/7,text="Graphs",font="Dubai 35",fill="black")

     
class Option(object):
    word = ""
    startMonth = "month"
    startDay = "day"
    startYear = "year"
    endMonth = "month"
    endDay = "day"
    endYear = "year"

    @staticmethod
    def draw(canvas,width,height):
        canvas.create_rectangle(0,0,width,height,fill="light grey",width=0)
        # stock name 
        canvas.create_text(width/2,height/5,text="Enter a stock",font="Dubai 20")
        canvas.create_rectangle(width/8,2.5*height/10,width*7/8,height*3.5/10,fill="white")
        canvas.create_text(width/2,height*3/10,text=Option.word,font="Dubai 20",fill="black")
        # dates 
        canvas.create_text(width*2/8,height*5/10,text="Starting Date",font = "Dubai 20",fill="black")
        canvas.create_text(width*6/8,height*5/10,text="Ending Date",font = "Dubai 20",fill="black")
        #start date boxes 
        canvas.create_rectangle(width*2/20,height*11/20,width*3.5/20,height*13/20,fill="white")
        canvas.create_rectangle(width*4/20,height*11/20,width*5.5/20,height*13/20,fill="white")
        canvas.create_rectangle(width*6/20,height*11/20,width*9/20,height*13/20,fill="white")
        # text for date 
        canvas.create_text(width*2.75/20,height*12/20,text=Option.startMonth,font = "Dubai 10",fill="black")
        canvas.create_text(width*4.75/20,height*12/20,text=Option.startDay,font = "Dubai 10",fill="black")
        canvas.create_text(width*7.5/20,height*12/20,text=Option.startYear,font = "Dubai 10",fill="black")
        #end date boxes 
        canvas.create_rectangle(width*11/20,height*11/20,width*12.5/20,height*13/20,fill="white")
        canvas.create_rectangle(width*13/20,height*11/20,width*14.5/20,height*13/20,fill="white")
        canvas.create_rectangle(width*15/20,height*11/20,width*18/20,height*13/20,fill="white")
        canvas.create_text(width*11.75/20,height*12/20,text=Option.endMonth,font = "Dubai 10",fill="black")
        canvas.create_text(width*13.75/20,height*12/20,text=Option.endDay,font = "Dubai 10",fill="black")
        canvas.create_text(width*16.5/20,height*12/20,text=Option.endYear,font = "Dubai 10",fill="black")
        
        # write visualize or go?
        canvas.create_rectangle(width*1.5/10,14*height/20,3.5*width/10,height*17/20,fill="light yellow")
        canvas.create_rectangle(6.5*width/10,14*height/20,8.5*width/10,height*17/20,fill="light pink")
        canvas.create_text(width*2.5/10,height*15.5/20,text="Candlestick",font="Dubai 20",fill="black")
        canvas.create_text(width*7.5/10,height*15.5/20,text="Solid Line",font="Dubai 20",fill="black")
    
        
        

class Portfolio(object):
    # to add in keypressed
    stocks = []
    moves = []
    numShares = []
    endDate = []
    endPrices = []
    earnings = []
    

    @staticmethod
    def drawEntry(canvas,width,height):
        # background
        title = ['Stock','Buy/Short','# of Shares','End date','End date price','Earnings','Graph']
        margin=width/15
        numRows = 11
        numCols = 7
        rowWidth = (height-2*margin)/numRows
        columnWidth =  (width-2*margin)/numCols
        canvas.create_rectangle(0,0,width,height,fill="wheat1")
        
       # optional pie chart? 
       # canvas.create_rectangle(width-width*.4,2*height/3,width-width/5,height*9/10,fill="cornflower blue")
       # canvas.create_text(.3*width,.8*height,text="Visualize Portfolio",font="Dubai 20")
       
        # rows in table 
        for i in range(numRows):
            canvas.create_rectangle(margin,margin+i*rowWidth,width-margin,margin+(i+1)*rowWidth,fill='light grey')
        # columns in table 
        for i in range(numCols):
            canvas.create_line((i+1)*columnWidth+margin,margin,(i+1)*columnWidth+margin,width-3.12*margin)
            
        # drawing things in table 
        for i in range(numCols):
            canvas.create_text(i*columnWidth+margin+columnWidth/2,rowWidth/2+margin,text=title[i],font="Calibri 10 bold")
        
        # graph buttons
        for i in range(1,numRows):
            canvas.create_rectangle(width-margin-columnWidth,margin+i*rowWidth,width-margin-columnWidth/2,margin+(i+1)*rowWidth,fill="light yellow")
            canvas.create_text(width-margin-3*columnWidth/4,margin+rowWidth*(2*i+1)/2,text='Candle',font='Calibri 7') 
            canvas.create_rectangle(width-margin-columnWidth/2,margin+i*rowWidth,width-margin,margin+(i+1)*rowWidth,fill='light pink')
            canvas.create_text(width-margin-columnWidth/4,margin+rowWidth*(2*i+1)/2,text="Solid",font='Calibri 7')
        
        # calculate and save buttons
        canvas.create_rectangle(width-4.75*margin,margin/6,width-2.875*margin,margin*5/6,fill="light blue")
        canvas.create_text(width-3.8*margin,margin/2,text='Calculate',font='Calibri 10 bold')
        canvas.create_rectangle(width-2.875*margin,margin/6,width-margin,margin*5/6,fill="light green")
        canvas.create_text(width-2*margin,margin/2,text='Save',font='Calibri 10 bold')
        
        # back button 
        canvas.create_rectangle(margin/3,margin/3,margin,margin*2/3,outline="black",width=1.5)
        canvas.create_rectangle(margin/2,margin*1.25/3,margin,margin*1.75/3,fill='green',outline='black',width=2)
        canvas.create_polygon(margin/2,margin/3,margin/3,margin/2,margin/2,margin*2/3,fill='green',outline='black',width=2)


class Graph(object):
    def __init__(self,company,width,height,startDate,endDate):
        self.company = company 
        self.width = width
        self.height = height 
        self.dates = quandl.get('WIKI/'+self.company,start_date=startDate,end_date=endDate)
        self.close = quandl.get('WIKI/'+self.company,start_date=startDate,end_date=endDate,column_index=4)
        self.displayDates = []
        self.solidCloseValues = []
        self.numOrigVal = 0
        self.numPredictedVal= 0
    
    # rows and number more to be predicted 
    def getDates(self):
        # Dates 
        
        #print (dates)
        #print (dates)
        #print( type(dates.index)) # type panda 
        #print(len(dates.index))
        # stack overflow for syntax tolist 
        #print(dates.index.tolist())
        #print(self.displayDates)
        #print (len(dates.index.tolist()))
        for d in self.dates.index.tolist():
            date = str(d)
            #print(date[:10])
            print('hi')
            self.displayDates.append((date[:10]))
    
    def addDates(self,predicted):
        for prediction in predicted:
            self.displayDates.append(prediction[0])
            #print (self.displayDates)
    
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
        #return self.solidCloseValues
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
        radius = 3
        margin = self.width/7
        increment = (self.width-2*margin)/len(self.displayDates)
        # background 
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
        
        # draw dates
        if self.displayDates[0][:4]!=self.displayDates[-1][:4]:
            dateTxt = "Years: " + self.displayDates[0][:4] + "-" + self.displayDates[-1][:4]
        else: 
            dateTxt = "Year: " + self.displayDates[0][:4]
        canvas.create_text(1.5*margin,margin-10,text= dateTxt,font="Dubai 15")
    
        # x-axis: dates and addpoints 
       # print('num predict',self.numPredictedVal)
       # print('dates',self.solidCloseValues)
        for i in range(len(self.displayDates)):
            xPos = i*increment + margin + startingPt
            yPos = yBase-(yIncrement/scale)* (self.solidCloseValues[i]-minimum)
            if i==self.numOrigVal-1:
                newLines.append((xPos,yPos))
                connectLines.append((xPos,yPos))
            elif i>self.numOrigVal-1:
                newLines.append((xPos,yPos))
            else:
                connectLines.append((xPos,yPos))
            canvas.create_line(xPos,self.height-margin,xPos,self.height-7*margin/8)
            # stack overflow for angle 
            if self.displayDates[i][5]=="0":
                txt = self.displayDates[i][6:]
            else:
                txt = self.displayDates[i][5:]
            canvas.create_text(xPos,self.height-70,text=txt,font="Calibri 8 bold",angle=90) 
        
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
        
        # side labels 
        canvas.create_text(margin/3,self.height/2,text="Closing Price",font="Dubai 20",angle=90)
        canvas.create_text(self.width/2,self.height-margin/3,text="Date",font = "Dubai 20")
        
        # back button 
        canvas.create_rectangle(margin/3,margin/3,margin,margin*2/3,outline="black",width=1.5)
        canvas.create_rectangle(margin/2,margin*1.25/3,margin,margin*1.75/3,fill='green',outline='black',width=2)
        canvas.create_polygon(margin/2,margin/3,margin/3,margin/2,margin/2,margin*2/3,fill='green',outline='black',width=2)
        
        # predict button 
        canvas.create_rectangle(self.width-margin,margin/3,self.width-margin/3,margin*2/3,fill="light green",width=1.5)
        canvas.create_text(self.width-2*margin/3,margin/2,text="PREDICT",font="Dubai 10")
        
        #title
        canvas.create_text(self.width/2,margin/2,text=self.company,font="Dubai 30")

        
                
            
class CandleStick(Graph):
    def __init__(self,company,width,height,startDate,endDate):
        super().__init__(company,width,height,startDate,endDate)
        self.open = quandl.get('WIKI/'+self.company,column_index=1)
        self.high = quandl.get('WIKI/'+self.company,column_index=2)
        self.low = quandl.get('WIKI/'+self.company,column_index=3)
        self.convertOpen = []
        self.convertHigh = []
        self.convertLow = []
        self.convertClose = []
        self.margin = self.width/7
        self.startY = self.height-self.margin
        self.startingPt = self.margin/2
        self.yBase = self.startY-self.startingPt
        self.minimum = None 
        self.yIncrement = (self.height-2*self.margin)/len(self.dates)
        self.increment = (self.width-2*self.margin)/len(self.dates)
        self.portfolio = False 
        
        
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
        #print(self.maxVal,self.minVal,self.minimum)
        #print('low',lowVal)
        #print('high',highVal)
        #print('scale',self.scale)
        
    def getLowValues(self):
        for val in self.low:
            for i in range(len(self.low[val])):
                #adjustPoints = yIncrement/scale * (closingValues[i]-minimum)
                value = self.low[val][i]
                newVal = self.yBase-(self.yIncrement/self.scale)*(value-self.minimum)
                #print (value,newVal)
                self.convertLow.append(newVal)
       # print('converted low',self.convertLow)
       # print ('low',self.low)
        
    def getHighValues(self):
        for val in self.high:
            for i in range(len(self.high[val])):
                value = self.high[val][i]
                newVal = self.yBase-(self.yIncrement/self.scale)*(value-self.minimum)
                self.convertHigh.append(newVal)
        
    def getOpenValues(self):
        for val in self.open:
            for i in range(len(self.open[val])):
                value = self.open[val][i]
                print (value)
                newVal = self.yBase-(self.yIncrement/self.scale)*(value-self.minimum)
                self.convertOpen.append(newVal)
        print(self.convertOpen[0])
        
    def getCloseValues(self):
        for val in self.solidCloseValues:           
                newVal = self.yBase-(self.yIncrement/self.scale)*(val-self.minimum)
                self.convertClose.append(newVal)
        print (self.solidCloseValues[0],self.convertClose[0])
        
    
    def drawCandleStick(self,canvas):
    
        canvas.create_rectangle(0,0,self.width,self.height,fill="light green",width=0)
        canvas.create_rectangle(self.margin,self.margin,self.width-self.margin,self.height-self.margin,fill="white")
        
        
        for i in range(len(self.displayDates)):
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
            if self.displayDates[i][5]=="0":
                txt = self.displayDates[i][6:]
            else:
                txt = self.displayDates[i][5:]
            canvas.create_text(xPos,self.height-70,text=txt,font="Calibri 8 bold",angle=90)
            
        # draw year 
        if self.displayDates[0][:4]!=self.displayDates[-1][:4]:
            dateTxt = "Years: " + self.displayDates[0][:4] + "-" + self.displayDates[-1][:4]
        else: 
            dateTxt = "Year: " + self.displayDates[0][:4]
        canvas.create_text(1.5*self.margin,self.margin-10,text= dateTxt,font="Dubai 15")
        
        for i in range(len(self.displayDates)):
            yPos = self.yBase-i*self.yIncrement
            val = self.minimum + i*self.scale
            canvas.create_line(7*self.margin/8,yPos,self.margin,yPos)
            canvas.create_text(7*self.margin/8,yPos,text=str(val),anchor= E,font="Calibri 10 bold")
            
        # side labels
        canvas.create_text(self.margin/3,self.height/2,text="Price",font="Dubai 20",angle=90)
        canvas.create_text(self.width/2,self.height-self.margin/3,text="Date",font = "Dubai 20")
        # title 
        canvas.create_text(self.width/2,self.margin/2,text=self.company,font="Dubai 30")
        
        # legend 
        canvas.create_rectangle(self.width-2.1*self.margin,self.margin/5,self.width-self.margin/5,self.margin*4/5)
        canvas.create_text(self.width-1.32*self.margin,self.margin*2/7,text="Tip of Candle: Highest price of that day",font='Dubai 7')
        canvas.create_text(self.width-1.24*self.margin,self.margin*3/7,text="Bottom of Candle: Lowest price of that day",font='Dubai 7')
        canvas.create_text(self.width-self.margin,self.margin*4/7,text="Closing Price higher than Opening Price",font='Dubai 7')
        canvas.create_text(self.width-self.margin,self.margin*5/7,text="Opening Price higher than Closing Price",font='Dubai 7')
        canvas.create_line(self.width-2*self.margin,self.margin*4/7,self.width-1.8*self.margin,self.margin*4/7,fill="white",width=3)
        canvas.create_line(self.width-2*self.margin,self.margin*5/7,self.width-1.8*self.margin,self.margin*5/7,fill="red",width=3)
        
        # back button
        canvas.create_rectangle(self.margin/3,self.margin/3,self.margin,self.margin*2/3,outline="black",width=1.5)
        canvas.create_rectangle(self.margin/2,self.margin*1.25/3,self.margin,self.margin*1.75/3,fill='green',outline='black',width=2)
        canvas.create_polygon(self.margin/2,self.margin/3,self.margin/3,self.margin/2,self.margin/2,self.margin*2/3,fill='green',outline='black',width=2)
## 112 website template 
def init(data):
    data.startState = True 
    data.drawCandle = False 
    data.drawSolidLine = False 
    data.width = 700
    data.height = 600 
    data.drawPredicted = False 
    data.Choice = False 
    data.enterStock = False 
    # entering options 
    data.startMonth = False 
    data.startDay = False
    data.startYear = False
    data.endMonth = False
    data.endDay = False
    data.endYear = False
    data.stockName = False
    data.portfolio = False 


def mousePressed(event, data):
    if data.Choice:
        if data.width/8<=event.x<=4*data.width/9 and 3*data.height/8<=event.y<=7*data.height/8:
            data.enterStock=True 
            data.Choice = False 
        elif 5*data.width/9<=event.x<=7*data.width/8 and 3*data.height/8<=event.y<=7*data.height/8:
            data.portfolio=True 
            data.Choice = False 
    elif data.enterStock:
        if data.width/8<=event.x<=data.width*7/8 and data.height*2.5/10<=event.y<=data.width*3.5/10:
            Option.word = ""
            data.stockName = True
            data.startDay,data.startYear,data.endMonth=False,False,False 
            data.endDay,data.endYear,data.startMonth = False,False,False
        if data.width*2/20<=event.x<=data.width*3.5/20 and data.height*11/20<=event.y<=data.height*13/20:
            Option.startMonth = ""
            data.startMonth = True 
            data.startDay,data.startYear,data.endMonth=False,False,False 
            data.endDay,data.endYear,data.stockName = False,False,False  
        if data.width*4/20<=event.x<=data.width*5.5/20 and data.height*11/20<=event.y<=data.height*13/20:
            Option.startDay = "" 
            data.startDay = True 
            data.startMonth,data.startYear,data.endMonth=False,False,False 
            data.endDay,data.endYear,data.stockName = False,False,False       
        if data.width*6/20<=event.x<=data.width*9/20 and data.height*11/20<=event.y<=data.height*13/20:
            Option.startYear="" 
            data.startYear = True 
            data.startDay,data.startMonth,data.endMonth=False,False,False 
            data.endDay,data.endYear,data.stockName = False,False,False
        if data.width*11/20<=event.x<=data.width*12.5/20 and data.height*11/20<=event.y<=data.height*13/20:
            Option.endMonth = "" 
            data.endMonth = True 
            data.startDay,data.startYear,data.startMonth=False,False,False 
            data.endDay,data.endYear,data.stockName = False,False,False
        if data.width*13/20<=event.x<=data.width*14.5/20 and data.height*11/20<=event.y<=data.height*13/20:
            Option.endDay = ""
            data.endDay = True 
            data.startDay,data.startYear,data.endMonth=False,False,False 
            data.startMonth,data.endYear,data.stockName = False,False,False
        if data.width*15/20<=event.x<=data.width*18/20 and data.height*11/20<=event.y<=data.height*13/20:    
            Option.endYear = ""
            data.endYear = True 
            data.startDay,data.startYear,data.endMonth=False,False,False 
            data.endDay,data.startMonth,data.stockName = False,False,False
        # buttons 
        if data.width*1.5/10<=event.x<=data.width*3.5/10 and data.height*14/20<=event.y<=data.height*17/20:
            data.drawCandle=True 
            sMonth = Option.startMonth
            sDay = Option.startYear
            eMonth = Option.endMonth
            eDay = Option.endDay
            if len(Option.startMonth)==1: sMonth="0"+Option.startMonth
            if len(Option.startDay)==1: sDay = "0"+Option.startDay
            if len(Option.endMonth)==1: eMonth= "0"+Option.endMonth
            if len(Option.endDay)==1: eDay = "0"+Option.endDay 
            endDate = Option.endYear+"-"+eMonth+"-"+eDay 
            startDate = Option.startYear+"-"+sMonth+"-"+sDay
            
            data.candle = CandleStick(Option.word,data.width,data.height,startDate,endDate)
            data.candle.getDates()
            data.candle.getClosingValues()
            data.candle.getScale()
            data.candle.getLowValues()
            data.candle.getHighValues()
            data.candle.getOpenValues()
            data.candle.getCloseValues()
            data.enterStock=False
        if (6.5*data.width/10)<=event.x<=(8.5*data.width/10) and (14*data.height/20)<=event.y<=(data.height*17/20):
            data.drawSolidLine=True 
            sMonth = Option.startMonth
            sDay = Option.startYear
            eMonth = Option.endMonth
            eDay = Option.endDay
            if len(Option.startMonth)==1: sMonth="0"+Option.startMonth
            if len(Option.startDay)==1: sDay = "0"+Option.startDay
            if len(Option.endMonth)==1: eMonth= "0"+Option.endMonth
            if len(Option.endDay)==1: eDay = "0"+Option.endDay 
            endDate = Option.endYear+"-"+eMonth+"-"+eDay 
            startDate = Option.startYear+"-"+sMonth+"-"+sDay
            data.line = Solid(Option.word,data.width,data.height,startDate,endDate)
            data.line.getDates()
            data.line.getClosingValues()
            data.enterStock=False 
    #else:
     #   if data.drawPredicted:
            # two days for now 
            # HARDCODED SOME PREDICTION FOR APPPLE FIX!!!
       #     predictedVal = RegressionModel.linearReg(2,5)
        #    print (predictedVal)
       #     data.line.addDates(predictedVal)
        #    data.line.predictedCloseValues(predictedVal)
            
            

def redrawAll(canvas, data):
    if data.startState:
        Cover.draw(canvas,data.width,data.height)
    elif data.Choice:
        Choice.draw(canvas,data.width,data.height)
    elif data.enterStock:
        Option.draw(canvas,data.width,data.height)
    elif data.enterStock==False and data.drawCandle==True:
        data.candle.drawCandleStick(canvas)
    elif data.enterStock==False and data.drawSolidLine==True:
        data.line.drawSolid(canvas)
    elif data.portfolio:
        Portfolio.drawEntry(canvas,data.width,data.height)
        
        

# press s for solid line graph
# press c for candlestick graph
# press b to go back to original state
# press p to predict  
def keyPressed(event, data):
    if event.keysym=="c":
        data.drawCandle= True 
        data.startState = False
        data.drawSolidLine = False
    # no more of this-- use button 
    elif event.keysym=="space":
        data.Choice = True 
        data.drawCandle= False  
        data.startState = False
        data.drawSolidLine = False
    elif event.keysym=="l":
        data.drawCandle= False 
        data.startState = False
        data.drawSolidLine = True 
    elif event.keysym=="s":
        data.drawCandle= False
        data.startState = True 
        data.drawSolidLine = False
    elif event.keysym=="p":
        data.drawPredicted = not data.drawPredicted 
       
    if data.enterStock:
        letter = event.keysym
        controlInput(data,letter)
        

def controlInput(data,letter):
    if data.stockName:
        if letter=="BackSpace" and len(Option.word)>0:
            Option.word=Option.word[:-1]
        elif letter in string.ascii_letters and len(Option.word)<10:
            Option.word+=letter.upper()
    elif data.startMonth:
        if letter=="BackSpace" and len(Option.startMonth)>0:
            Option.startMonth=Option.startMonth[:-1]
        elif letter in string.digits and len(Option.startMonth)<2:
            Option.startMonth+=letter
    elif data.startDay:
        if letter=="BackSpace" and len(Option.startDay)>0:
            Option.startDay=Option.startDay[:-1]
        elif letter in string.digits and len(Option.startDay)<2:
            Option.startDay+=letter
    elif data.startYear:
        if letter=="BackSpace" and len(Option.startYear)>0:
            Option.startYear=Option.startYear[:-1]
        elif letter in string.digits and len(Option.startYear)<4:
            Option.startYear+=letter
    elif data.endMonth:
        if letter=="BackSpace" and len(Option.endMonth)>0:
            Option.endMonth=Option.endMonth[:-1]
        elif letter in string.digits and len(Option.endMonth)<2:
            Option.endMonth+=letter
    elif data.endDay:
        if letter=="BackSpace" and len(Option.endDay)>0:
            Option.endDay=Option.endDay[:-1]
        elif letter in string.digits and len(Option.endDay)<2:
            Option.endDay+=letter
    elif data.endYear:
        if letter=="BackSpace" and len(Option.endYear)>0:
            Option.endYear=Option.endYear[:-1]
        elif letter in string.digits and len(Option.endYear)<4:
            Option.endYear+=letter
            

    
    
    
         
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
