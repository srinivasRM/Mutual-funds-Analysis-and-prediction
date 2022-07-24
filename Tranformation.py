import pandas as pd 
import numpy as np 

df = pd.read_excel('raw_data.xlsx')
df = df.drop(columns = ['Unnamed: 0'])

df = df.drop(columns = ['average_maturity','yield_to_maturity','pe','pb','Exit_Load_lst','link_of_the_funds','name_of_the_fund','name_of_the_fund_lst'])

#AUM column has values in the format of ₹1,711.78Cr 
#We need to split it now. 
# df['aum_funds_individual_lst'] = df['aum_funds_individual_lst'].apply(map(lambda x:x.split('Cr')[0].split('₹')[1].replace(',','')))
lst = []
lst_1 = []
for x in range(0,len(df['aum_funds_individual_lst'])):
    try:
        lst.append(float(df['aum_funds_individual_lst'][x].replace('₹','').replace('Cr','').replace(',','')) )
    except ValueError:
        lst.append(np.nan)
        
for y in range(0,len(df['nav_funds_individual_lst'])):  
    if df['nav_funds_individual_lst'][y].isnumeric() == False:
        lst_1.append(df['nav_funds_individual_lst'][y].replace(',',''))
    else :
        lst_1.append(df['nav_funds_individual_lst'][y])


df['aum_funds_individual_lst'] = lst
df['nav_funds_individual_lst'] = lst_1

df.to_excel('cleaned_data.xlsx')        


df['type_of_fund'].unique()    