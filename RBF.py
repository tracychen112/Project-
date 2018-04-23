#This code just implements the k-means clustering algorithm and computes the standard deviations. 
#It references to https://pythonmachinelearning.pro/using-neural-networks-for-regression-radial-basis-function-networks/

import random
import math
import numpy as np


dates = []
prices = []
start_month = 1

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(31*(int(row[0].split('/')[0])-start_month)+int(row[0].split('/')[1]))
            prices.append(float(row[1]))
    return

def rbf(x, c, s):
    return math.exp(-1 / (2 * s**2) * (x-c)**2)


# https://codeselfstudy.com/blogs/how-to-calculate-standard-deviation-in-python
def standard_deviation(lst, population=True):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
 
    if population is True:
        variance = ssd / num_items
    else:
        # WHY HERE SUBTRACT 1?!
        variance = ssd / (num_items - 1)
    sd = math.sqrt(variance)
    return sd


def kmeans(X, k):
    clusters = []
    
    kk = random.sample(range(len(X)), k)
    
    for i in kk:
        clusters.append(X[i])
        
    
    prevClusters = clusters.copy()
    stds = [0]*k

    converged = False
    distances = [[0 for i in range(len(clusters))] for j in range(len(X))]

    v = 0
    while not converged:

        """
        compute distances for each cluster center to each point 
        where (distances[i, j] represents the distance between the ith point and jth cluster)
        """
        
        # calculate distance
        for i in range(len(X)):
            for j in range(len(clusters)):
                distances[i][j] = abs(X[i]-clusters[j])

        closestCluster = [[0 for i in range(len(X))] for j in range(len(clusters))]
        # loop through distance, and put x[i] to closetCluster
        for i in range(len(X)):
            smallest = 0
            index = 0
            for j in range(len(clusters)):
                if ( j == 0 ) :
                    smallest = distances[i][j]
                    index = 0
                else :
                    if smallest > distances[i][j]:
                        smallest = distances[i][j]
                        index = j
            # put the x[i] to closestCluster
            closestCluster[index][i]=X[i]

        # update cluster
        for i in range(len(clusters)):
            total = 0
            count = 0
            for j in range(len(X)):
                if closestCluster[i][j] > 0 :
                    total += closestCluster[i][j]
                    count +=1
            mean = int( total/count)
            clusters[i]=mean

        # converge if clusters haven't moved
        sum = 0
        for i in range (len(clusters) ):
           sum += (clusters[i]-prevClusters[i])**2
        converged = math.sqrt(sum)  < 1e-6
        prevClusters = clusters.copy()

     
        

    # calculate distance
    for i in range(len(X)):
        for j in range(len(clusters)):
            distances[i][j] = abs(X[i]-clusters[j])

    closestCluster = [[0 for i in range(len(X))] for j in range(len(clusters))]
    # loop through distance, and put x[i] to closetCluster
    for i in range(len(X)):
        smallest = 0
        index = 0
        for j in range(len(clusters)):
            if ( j == 0 ) :
                smallest = distances[i][j]
                index = 0
            else :
                if smallest > distances[i][j]:
                    smallest = distances[i][j]
                    index = j
        # put the x[i] to closestCluster
        closestCluster[index][i]=X[i]

    clustersWithNoPoints = []
    for i in range(k):
        newList = []
        for j in range (len(closestCluster[i])):
            if closestCluster[i][j] > 0 :
               newList.append(closestCluster[i][j])
        
       # pointsForCluster = X[closestCluster == i]
        if len(newList) < 2:
            # keep track of clusters with no points or 1 point
            clustersWithNoPoints.append(i)
            continue
        else:
            stds[i] = standard_deviation(newList)

    return clusters, stds


class RBFNet(object):
    """Implementation of a Radial Basis Function Network"""
    def __init__(self, k=2, lr=0.01, epochs=100, rbf=rbf, inferStds=True):
        self.k = k
        self.lr = lr
        self.epochs = epochs
        self.rbf = rbf
        self.inferStds = inferStds

        # the only two lines using numpy because it's too complicated to implement
        #self.w = np.random.randn(k).tolist()
        #self.b = np.random.randn(1).tolist()
        
        # Box muller method- generate two independent normal random variables
        #https://stats.stackexchange.com/questions/16334/how-to-sample-from-a-normal-distribution-with-known-mean-and-variance-using-a-co 
        self.w = []
        self.b = [] 
        if int(k)%2==1:
            numGenerate = int(k)+1
        else:
            numGenerate = int(k)
        for i in range(k):
            U1 = random.uniform(0,1)
            U2 = random.uniform(0,1)
            z1 = math.sqrt(-2*math.log(U1,math.e))*math.cos(2*math.pi*U2)
            z2 = math.sqrt(-2*math.log(U1,math.e))*math.sin(2*math.pi*U2)
            self.w.extend([z1,z2])
        # remove extra number if necessary 
        if k%2==1: self.w.pop()
        # for b only 
        U1 = random.uniform(0,1)
        U2 = random.uniform(0,1)
        z1 = math.sqrt(-2*math.log(U1,math.e))*math.cos(2*math.pi*U2)
        z2 = math.sqrt(-2*math.log(U1,math.e))*math.sin(2*math.pi*U2)
        self.b.extend([z1,z2])

    def fit(self, X, y):
       
        # compute stds from data
        self.centers, self.stds = kmeans(X, self.k)
        
        for epoch in range(self.epochs):
            for i in range(len(X)):
                # forward pass
                a1 = [self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)]
 
                #compute a.T.dot(self.w)
                dotSum = 0
                for j in range(len(a1)):
                    dotSum += a1[j] * self.w[j]
                F = dotSum + self.b[0]
                
                loss = (y[i] - F) ** 2
                error = -(y[i] - F)

                #online update
                for t in range(self.k):
                    self.w[t] = self.w[t] - self.lr *  a1[t] * error

                self.b[0] = self.b[0] - self.lr * error


    def predict(self, X):
        y_pred = []
        for i in range(len(X)):
            a = [self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)]
            
            #compute a.T.dot(self.w)
            dotSum = 0
            for j in range(len(a)):
                dotSum += a[j] * self.w[j]
                
            # F = a.T.dot(self.w) + self.b  
            F = dotSum + self.b[0]            
            
            y_pred.append(F)
        
        return y_pred