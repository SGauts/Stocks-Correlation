import pandas as pd

import numpy as np

import math

 

# Importing the dataset

 

data123 = pd.read_csv('data123.csv')

banks= pd.read_csv('yesbank.csv')

 

X = data123.iloc[:,4].values

Y = banks.iloc[:,8].values

 

maxlim= len(Y)

n=9

nifty= np.zeros(n-1)

niftysquare=np.zeros(n-1)

bank=np.zeros(n-1)       #(X-Xmean)^2

banksquare=np.zeros(n-1) #(Y-Ymean)^2

multi=np.zeros(n-1)

 

nifavg=0

bankavg=0

varianceNifty=0

STDnifty=0

STDbank=0

variancebank=0

covariance=0

correlation=0

Rsquare=0

c1=0

 

t=1

while (maxlim-8)>0:

   

    for i in range(0,n-1):           #Calculating Returns for Nifty and Bank

        nifty[i]=X[i+1+c1]/X[i+c1]   

        nifty[i]= math.log(nifty[i])

        nifavg=nifty[i]+nifavg;

       

        bank[i]=Y[i+1]/Y[i]

        bank[i]=math.log(bank[i])

        bankavg=bankavg+bank[i]

        pass

   

    nifavg=nifavg/(n-1)             #Calculating Mean Return

    bankavg=bankavg/(n-1)

   

    for i in range(0,(n-1)):          #Calculating X-Xmean and (X-Xmean)^2 and same with Y

        nifty[i]=nifty[i]-nifavg

        niftysquare[i]=math.pow(nifty[i],2)

        varianceNifty=varianceNifty+niftysquare[i]

       

        bank[i]=bank[i]-bankavg

        banksquare[i]=math.pow(bank[i],2)

        variancebank=variancebank+banksquare[i]

        multi[i]=nifty[i]*bank[i]

        covariance=covariance+multi[i]

        pass

   

    varianceNifty=varianceNifty/(n-2)   #Variance of X

    STDnifty = math.sqrt(varianceNifty)   #Standard Deviation of X

    variancebank=variancebank/(n-2)         #Variance of Y

    STDbank=math.sqrt(variancebank)       #Standard deviation of Y

    covariance=covariance/(n-2)           #Covariance

   

    correlation=covariance/(STDbank*STDnifty)   #correlation

    Rsquare=math.pow(correlation,2)            #R-Square value

   

    print("Correlation for batch ", t, " is ",correlation )

    print("RSquare  for batch ", t, "is ",Rsquare )

    print("\n")

    pass

    t=t+1

    c1=c1+8

    maxlim=maxlim-8

pass