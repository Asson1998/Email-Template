import pandas as pd
import csv
import re
j=0
i=0
i=[]
# 1.Fetch the Detail like name, email, email Body, email subject and create email template for each individuals. 
data=pd.read_csv('sample_email.csv',encoding='latin1')
print(data.loc[:,'first_name'])
# print(data.iloc[0,1])
IND=int(input('\nEnter the index value of the person you want to send email to'))
RN=input('\nEnter reciver name')

print('\nEMAIL TEMPLATE FOR THE PERSON IS:-')
print('Email to :' + str(data.iloc[IND,10]))
print('Subject Line:'+ str(data.iloc[IND,11]))
print('Hi ' + str(data.iloc[IND,0])+' ' + str(data.iloc[IND,1]) + ',') 
print(str(data.iloc[IND,12]))
print('\nThanks,')
print('\n'+str(RN))

# 2. Check and fetch email address from the email body section if any present and store it in another CSV. 
with open ('Emails.csv','w',newline='') as file:
    while j<49:
        
        
        writer = csv.writer(file)
        writer.writerow([data.iloc[j,10]])
        j=j+1

# 3. Check and fetch mail number from the email body section if any present and store it in another CSV.
with open ('Mail_numbers.csv','w+',newline='') as file:
    for line in data.iloc[:,12]:
        
        y=re.findall('\S\S\S\S\S\s\S[0-9]+-[0-9]+',line)
        z=re.findall('\S\S\S\S\S\S[0-9]+-[0-9]+',line)    
        
        for Y in y:
            if len(Y)!=0:
                # print(y)
                writer = csv.writer(file)
                writer.writerow([Y])
        for Z in z:     
            if len(z)!=0:
                # print(z)
                writer = csv.writer(file)
                writer.writerow([Z])
            
                
   