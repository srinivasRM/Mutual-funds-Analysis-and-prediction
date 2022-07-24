from sqlalchemy import create_engine
import pandas as pd
import datetime as dt
import os


# format: SQLNAME://user:pass@host/db

engine = create_engine('postgresql://akmsvuudvojpti:35e7628d30691d2b61384f7ab2e97a883f60b27c3922790ac79cc03268656843@ec2-3-219-229-143.compute-1.amazonaws.com/dbae31ljqo7na3')

#Clearing the previous data and inserting current days data
query_dump = '''
DROP TABLE IF EXISTS "MutualFundsRawData" CASCADE;
'''
result = engine.execute(query_dump)

df = pd.read_excel('cleaned_data.xlsx')

# To send the data to Database at Heroku 

df['Date of Extraction'] = str(dt.date.today())  

df.to_sql('MutualFundsRawData', con=engine) #Run the current line to send a dataframe to the Database

#df = df.drop(columns = ['index','Unnamed: 0'])


