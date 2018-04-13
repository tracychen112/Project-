import quandl
quandl.ApiConfig.api_key = 'CQUhXPCW3sqs92KDd1rD'
#curl "https://www.quandl.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY,IWM&api_key=CQUhXPCW3sqs92KDd1rD"
#import matplotlib.pyplot as plt
#data <- Quandl.datatable('MER/F1', compnumber="39102")

data = quandl.get('WIKI/FB') 
#print(data.index)
print(data)
#print(data)
#data2 = quandl.get('WIKI/AAPL',limit=1,column_index=3)    # this will get 1949 records
#print(data2)
#print(data.head(5))
#print(data.tail(5))
#print(data.count())
"""
plt.plot(data.index, data['Adj. Close'], 'g')
plt.title('Tesla Stock Price')
plt.ylabel('Price ($)');
plt.show();
"""

#data = quandl.get("WIKI/TSLA", start_date="2018-03-20", end_date="2018-04-10")
#print(data.head(5))
#print(data.tail(5))


#quandl.bulkdownload(data)