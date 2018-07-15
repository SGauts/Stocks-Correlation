import pandas as pd

import numpy as np

import math

 

# Importing the dataset

Names=["bobbank.csv","yesbank.csv","sbibank.csv", "kotakbank.csv","Axisbank.csv",

       "IDFCbank.csv","pnbbank.csv"]

CorrelationArray=np.zeros(len(Names))

RsquareArray=np.zeros(len(Names))

 

CorrelationArrayB=np.zeros(len(Names)*len(Names))

RsquareArrayB=np.zeros(len(Names)*len(Names))

#for storing the various co-variance

zil=0;

while zil<49:

    for m in range(0,len(Names)):

        for mk in range(0,len(Names)):

            data123 = pd.read_csv(Names[mk])

            bank = pd.read_csv(Names[m])

           

            X = data123.iloc[:,8].values

            Y = bank.iloc[:,8].values

            n=len(bank)

           

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

           

            for i in range(0,(n-1)):           #Calculating Returns for Nifty and Bank

                nifty[i]=X[i+1]/X[i]   

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

            CorrelationArray[m]=correlation;

            RsquareArray[m]=Rsquare

            CorrelationArrayB[zil]=correlation;

            RsquareArrayB[zil]=Rsquare

            print("Correlation of ",Names[m]," with ", Names[mk]," is: ",CorrelationArray[m] )

            print("RSquare of ",Names[m]," with ", Names[mk]," is: ",RsquareArray[m] )

            print("\n")

            

            zil=zil+1

        pass

    pass

pass

 

import json

 

kab = 0

 

 

while kab<49:

    for abc in range(0,len(Names)):

        for jkl in range(0,len(Names)):

       

            data = {

                        "Correlation of ": Names[abc],

                        "with": Names[jkl],

                        "is: ": CorrelationArrayB[kab],

                 

                    }

            data1={

                      "RSquare of ": Names[abc],

                       "with": Names[jkl],

                       "is: ": RsquareArrayB[kab],

                   

                    }

           

            #json.dumps() method turns a Python data structure into JSON:

            jsonData = json.dumps(data)

            z=json.dumps(data1)

            print(jsonData)

            print(z)

            with open('Correlation.json', 'a') as i:

                json.dump(jsonData, i, indent=1)

                json.dump(z,i, indent=1)

                kab=kab+1

                pass

        pass

 

pass