#Importing Required libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.error import HTTPError
import numpy as np

print('Started')
returs_of_the_funds_lst = []
name_of_the_fund_lst = []
risk_of_the_fund_lst = []
type_of_fund_lst = []
link_of_the_funds_lst  = []
y=0
for x in range(0,71,1):
    page = requests.get("https://groww.in/mutual-funds/filter?q=&fundSize=&pageNo="+str(x)+"&sortBy=0")
    soup = BeautifulSoup(page.content, 'html.parser')
    name_of_the_fund = soup.find_all('div',class_="fs14 clrText fw500 f22LH34 f22Mb4 truncate")
    risk_of_the_fund = soup.find_all('div',class_="fs12 fw500 clrSubText f22Ls2")
    type_of_fund = soup.find_all('div',class_="fs12 fw500clrSubText f22Ls2")
    returs_of_the_funds = soup.find_all('div',class_="fs14 clrText fw500 center-align f22Mb4")
    link_of_the_funds = soup.find_all('a',class_="pos-rel f22Link" )
    for x in range (0,len(name_of_the_fund)):
            name_of_the_fund_lst.append(str(name_of_the_fund[x]).split('>')[1].split('<')[0])
            risk_of_the_fund_lst.append(str(risk_of_the_fund[x]).split('>')[1].split('<')[0])
            type_of_fund_lst.append(str(type_of_fund[x]).split('>')[1].split('<')[0])
            link_of_the_funds_lst.append('https://groww.in/'+str(str(link_of_the_funds[x]).split(' ')[3].split('=')[1].split('"/')[1].split('"')[0]))


returs_of_the_funds_lst  = []
for x in range(0,71,1):
    page = requests.get("https://groww.in/mutual-funds/filter?q=&fundSize=&pageNo="+str(x)+"&sortBy=0")
    soup = BeautifulSoup(page.content, 'html.parser')
    returs_of_the_funds = soup.find_all('div',class_="fs14 clrText fw500 center-align f22Mb4")
    for x in range(0,len(returs_of_the_funds)):
            returs_of_the_funds_lst.append(str(returs_of_the_funds[x]).split('>')[1].split('<')[0])

one_year_returns = []
three_year_returns = []
five_year_returns = []
for x in range(0,len(returs_of_the_funds_lst),3):
    one_year_returns.append(returs_of_the_funds_lst[x])
    three_year_returns.append(returs_of_the_funds_lst[x+1])
    five_year_returns.append(returs_of_the_funds_lst[x+2])

aum_funds_individual_lst = []
nav_funds_individual_lst = []
Exit_Load_lst = []
rating_of_funds_individual_lst = []
minimum_funds_individual_lst = []
Expense_Ratio_lst = []
Stamp_Duty_lst = []
for x in range(0,len(link_of_the_funds_lst)):
    page = requests.get(link_of_the_funds_lst[x])
    soup = BeautifulSoup(page.content, 'html.parser')
    common_funds_individual = soup.find_all('td',class_="fd12Cell clrText130 fs16 fw500")
    Expense_Ratio = soup.find_all('h3',class_="fs16 fw500 ot654subHeading")
    #Exit load string holger
    exit_funds_individual = soup.find_all('p',class_="fs16")
    #AUM extractor 
    aum_funds_individual_lst.append(str(common_funds_individual).split('''">''')[-1].split('</td>')[0])
    #Nav Extractor
    nav_funds_individual_lst.append(str(common_funds_individual).split('</td>')[0].split('>₹')[-1])
    #Minimum amount to be invested
    try:
        minimum_funds_individual_lst.append(float(str(common_funds_individual).split('>₹')[2].split('</')[0].replace(',','').replace('Cr','')))
    except IndexError:
        minimum_funds_individual_lst.append(np.nan)
        
    #Rating extractor
    rating_of_funds_individual = soup.find_all('td',class_="fd12Cell valign-wrapper clrText130 fs16 fw500 fd12Ratings")
    rating_of_funds_individual_lst.append(str(rating_of_funds_individual).split('">')[1].split('<')[0])
    
    #Extracting Expense ration from the website
    try:
        Expense_Ratio_lst.append(str(Expense_Ratio[0]).split('>')[2].split('%')[0])
        Exit_Load_lst.append(str(exit_funds_individual[1]).split('>')[1].split('<')[0])
    except IndexError:
        Expense_Ratio_lst.append(np.nan)
        Exit_Load_lst.append(np.nan)

scheme_code = []
for x in link_of_the_funds_lst:
    page = requests.get(x)
    soup = BeautifulSoup(page.content, 'html.parser')
    code = soup.find_all('script')
    index = str(code).find('scheme_code')
    holder = str(code)[index:index+35:1]
    scheme_code.append(holder.split('"')[2])


# page = requests.get(link_of_the_funds_lst[x])
# soup = BeautifulSoup(page.content, 'html.parser')
search_id = []
expense_ratio = []
category = []
sub_category = []
aum = []
pe = []
pb = []
debt_per = []
equity_per = []
average_maturity = []
yield_to_maturity = []
for x in scheme_code:
    try:
        df = pd.read_json('https://groww.in/v1/api/data/mf/web/v1/scheme/portfolio/'+str(x)+'/stats')
        pe.append(df['pe']['equity'])
        pb.append(df['pb']['equity'])
        debt_per.append(df['debt_per']['equity'])
        equity_per.append(df['equity_per']['equity'])
        average_maturity.append(df['average_maturity']['equity'])
        yield_to_maturity.append(df['yield_to_maturity']['equity'])
        # print(x)
    except KeyError:
        pe.append(np.nan)
        pb.append(np.nan)
        debt_per.append(np.nan)
        equity_per.append(np.nan)
        average_maturity.append(np.nan)
        yield_to_maturity.append(np.nan)    


analysis = {
'name_of_the_fund_lst':name_of_the_fund_lst,
'aum_funds_individual_lst':aum_funds_individual_lst,
'nav_funds_individual_lst':nav_funds_individual_lst,
'Exit_Load_lst':Exit_Load_lst,
'rating_of_funds_individual_lst':rating_of_funds_individual_lst,
'minimum_funds_individual_lst':minimum_funds_individual_lst,
'pe':pe,
'pb':pb,
'debt_per':debt_per,
'equity_per':equity_per,
'average_maturity':average_maturity,
'yield_to_maturity':yield_to_maturity,
'name_of_the_fund': name_of_the_fund_lst ,
'risk_of_the_fund':risk_of_the_fund_lst,
'type_of_fund':type_of_fund_lst ,
'one_year_returns':one_year_returns,
'three_year_returns':three_year_returns,
'five_year_returns':five_year_returns,
'link_of_the_funds':link_of_the_funds_lst
}

analysis_tables = pd.DataFrame(analysis)

analysis_tables.to_excel("raw_data.xlsx")

print('Raw data has been extracted!')