from sqlalchemy import create_engine
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
 
# df = pd.read_excel('cleaned_data.xlsx')
# # format: SQLNAME://user:pass@host/db
engine = create_engine('postgresql://akmsvuudvojpti:35e7628d30691d2b61384f7ab2e97a883f60b27c3922790ac79cc03268656843@ec2-3-219-229-143.compute-1.amazonaws.com/dbae31ljqo7na3')

#To send the data to Database at Heroku 
# df.to_sql('GraphicsCardTable', con=engine) Run the current line to send a dataframe to the Database

query = '''
select * from "GraphicsCardTable"
'''

df = pd.read_sql_query(query, engine)

df = df.drop(columns = ['index','Unnamed: 0'])


df.to_excel('cleaned_data.xlsx')









