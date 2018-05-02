# Websites referenced 
# https://machinelearningmastery.com/implement-logistic-regression-stochastic-gradient-descent-scratch-python/
# https://www.thesisscientist.com/docs/E-Booklets/cb4818b7-e718-4d37-9778-549fe427d2b2
import quandl
from math import exp


l_rate = 0.0001
n_epoch = 300
#name = 'X'

def getData(name):
    lst = []
    data = quandl.get('WIKI/'+name,start_date='2017-01-01',end_date='2018-03-01',column_index=4)
    for d in data:
        for i in range(len(data[d])):
            lst.append(data[d][i])
    
    # train 
    dataSet = [] 
    for i in range(1,len(lst)-2):
        if (lst[i+1] < lst[i+2]):
            dataSet.append([lst[i+2],lst[i+1],lst[i],1])
        else:
            dataSet.append([lst[i+2],lst[i+1],lst[i],0])
    return dataSet


# three functions below are copied from this url 
#https://machinelearningmastery.com/implement-logistic-regression-stochastic-gradient-descent-scratch-python/

# Make a prediction with coefficients
def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)-1):
        yhat += coefficients[i + 1] * row[i]
    return 1.0 / (1.0 + exp(-yhat))

# Estimate logistic regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
    coef = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            yhat = predict(row, coef)
            error = row[-1] - yhat
            sum_error += error**2
            coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
            for i in range(len(row)-1):
                coef[i + 1] = coef[i + 1] + l_rate * error * yhat * (1.0 - yhat) * row[i]
        #print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return coef
    
def getTest(name):
    dataSet = []
    data = quandl.get('WIKI/'+name,start_date='2018-03-20',end_date='2018-03-27',column_index=4)
    tempData = []
    
    for d in data:
        for i in range(len(data[d])):
            tempData.append(data[d][i])

    for i in range(1,len(tempData)-2):
        dataSet.append([tempData[i+2],tempData[i+1],tempData[i]])
    return dataSet


def logistic_regression(name,l_rate=0.0001, n_epoch=300):
    predictions = list()
    test = getTest(name)
    train = getData(name)
    coef = coefficients_sgd(train, l_rate, n_epoch)
    for row in test:
        yhat = predict(row, coef)
        yhat = round(yhat)
        predictions.append(yhat)
    return(predictions)


    
