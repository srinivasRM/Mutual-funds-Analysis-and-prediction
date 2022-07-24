#Importing all the libraries 
# This for building the front end for user interaction 
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn import preprocessing  
import seaborn as sns


#datetime and scheduler were used to run a function everyday on a given particular time
# import schedule
import datetime as dt

#For reading image files 
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

#Title for the web app 
st.markdown("<h1 style='text-align: center; color: white;'> Mutual Funds Predcition And Analysis 📈</h1>", unsafe_allow_html=True)

def visualization():

    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11 = st.tabs(["Chart 1", "Chart 2", "Chart 3","Chart 4","Chart 5","Chart 6","Chart 7","chart 8","chart 9","chart 10",'data'])
    df = pd.read_excel('cleaned_data.xlsx')
    with tab1:
        st.subheader('Report Created by matplotlib and Seaborn')
        figure, axes = plt.subplots(2, 2, figsize=(20,10))
        figure.suptitle('Date - ' + str(dt.date.today()) +'report')
        sns.barplot(ax = axes[0,0],x='type_of_fund', y='one_year_returns', data=df).set(title='type of fund vs one year returns')
        sns.barplot(ax = axes[0,1],x='type_of_fund', y='three_year_returns', data=df).set(title='type of fund type vs three year returns')
        sns.barplot(ax = axes[1,0],x='type_of_fund', y='five_year_returns', data=df).set(title='type of fund vs five year returns')
        sns.scatterplot(ax = axes[1,1 ],x='type_of_fund', y='aum_funds_individual_lst', data=df).set(title='type of fund vs aum of the funds ')
        st.pyplot(figure)


    with tab2:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='three_year_returns', y='five_year_returns', data=df).set(title='Three year returns vs Five Year returns')
        # To show the plot
        st.pyplot(fig)


    with tab3:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='one_year_returns', y='five_year_returns', data=df).set(title='One year returns vs Five year returns ')
        # To show the plot
        st.pyplot(fig)

    with tab4:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='one_year_returns', y='three_year_returns', data=df).set(title='One year returns vs Three year returns ')
        # To show the plot
        st.pyplot(fig)
    with tab5:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='one_year_returns', y='aum_funds_individual_lst', data=df).set(title='AUM of funds vs One year returns ')
        # To show the plot
        st.pyplot(fig)
    with tab6:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='three_year_returns', y='aum_funds_individual_lst', data=df).set(title='AUM of funds vs Three year returns ')
        # To show the plot
        st.pyplot(fig)        
    with tab7:
        fig, ax = plt.subplots()
        ax = sns.scatterplot(x='five_year_returns', y='aum_funds_individual_lst', data=df).set(title='AUM of funds vs Five year returns ')
        # To show the plot
        st.pyplot(fig)    

    with tab8:
        st.subheader('Debt percentage with vs and aum')
        figure, axes = plt.subplots(2, 2, figsize=(20,10))
        figure.suptitle('Date - ' + str(dt.date.today()) +'report')
        sns.scatterplot(ax = axes[0,0],x='debt_per', y='one_year_returns', data=df).set(title='debt percentage vs one year returns')
        sns.scatterplot(ax = axes[0,1],x='debt_per', y='three_year_returns', data=df).set(title='debt percentage type vs three year returns')
        sns.scatterplot(ax = axes[1,0],x='debt_per', y='five_year_returns', data=df).set(title='debt percentage vs five year returns')
        sns.scatterplot(ax = axes[1,1 ],x='debt_per', y='aum_funds_individual_lst', data=df).set(title='debt percentagevs aum of the funds ')
        st.pyplot(figure)
    with tab9:
        st.subheader('Equity percentage with vs and aum')
        figure, axes = plt.subplots(2, 2, figsize=(20,10))
        figure.suptitle('Date - ' + str(dt.date.today()) +'report')
        sns.scatterplot(ax = axes[0,0],x='equity_per', y='one_year_returns', data=df).set(title='Equity percentage vs one year returns')
        sns.scatterplot(ax = axes[0,1],x='equity_per', y='three_year_returns', data=df).set(title='Equity percentage type vs three year returns')
        sns.scatterplot(ax = axes[1,0],x='equity_per', y='five_year_returns', data=df).set(title='Equity percentage vs five year returns')
        sns.scatterplot(ax = axes[1,1 ],x='equity_per', y='aum_funds_individual_lst', data=df).set(title='Equity percentagevs aum of the funds ')
        st.pyplot(figure)  
    with tab10:
        st.subheader('Report Created by Tableau')
        image = Image.open('DASHBOARD FOR MUTUAL FUNDS.jpg')
        st.image(image)
    with tab11:
        st.table(df.head(10))    




def One_year_returns_predictions():
    st.subheader('One year returns predictions')

    with st.form(key='my_form_one'):

        user_AUM = st.number_input(label ='Enter the AUM of the mutual fund')

        user_NAV = st.number_input(label ='Enter the NAV of the mutual fund')

        user_rating  = st.multiselect('Select the rating of the fund', ['1', '2', '3', '4','5'])

        user_equity = st.number_input(label ='Enter the equity percentage of the mutual fund(0 to 100) based on this we debt percentage will be automatically calculated', min_value=0, max_value=100)

        user_debt = 100-user_equity

        risk_of_the_fund_user = st.multiselect('Select the rating of the fund', ['Very High', 'High', 'Moderately High', 'Moderate',
            'Low to Moderate', 'Moderately Low', 'Low'])

        type_of_fund  =  st.multiselect('Select the type of the fund', ['Equity', 'Other', 'Hybrid', 'Solution Oriented', 'Debt']) 
    

        three_year_returns_user =  st.number_input(label ='Enter the three year returns of the mutual fund')

        five_year_returns_user =  st.number_input(label ='Enter the five year returns of the mutual fund')

        submitted = st.form_submit_button('Submit')
        
        if submitted:

            le = preprocessing.LabelEncoder()
            le.classes_ = np.load('classes.npy',allow_pickle=True)

            user_rating = le.fit_transform(user_rating)
            type_of_fund = le.fit_transform(type_of_fund)
            risk_of_the_fund_user = le.fit_transform(risk_of_the_fund_user)

            with open('lst_transform.pkl', 'rb') as f:
                mynewlist = pickle.load(f)
           
            analysis = {

            'aum_funds_individual_lst':user_AUM/mynewlist[0],
            'nav_funds_individual_lst':user_NAV,
            'rating_of_funds_individual_lst':user_rating,
            'debt_per':user_debt/mynewlist[1],
            'equity_per':user_equity/mynewlist[3],
            'risk_of_the_fund':risk_of_the_fund_user,
            'type_of_fund':type_of_fund ,
            'three_year_returns':three_year_returns_user/mynewlist[4],
            'five_year_returns':five_year_returns_user/mynewlist[5],
            }

            prediction_tables = pd.DataFrame(analysis)   

            pickled_model = pickle.load(open('model_one_year_returns.pkl', 'rb'))
            prediction = pickled_model.predict(prediction_tables)

            if prediction <= 0:           
                st.metric(label="One Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)+(prediction/mynewlist[2])) + '%')
            else :
                st.metric(label="One Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)-(prediction/mynewlist[2])) + '%')

def Three_year_returns_predictions():
    st.subheader('Three year returns predictions')

    with st.form(key='my_form_three'):

        user_AUM = st.number_input(label ='Enter the AUM of the mutual fund',value  = 1711.78 )

        user_NAV = st.number_input(label ='Enter the NAV of the mutual fund',value  =127.22)

        user_rating  = st.multiselect('Select the rating of the fund', ['1', '2', '3', '4','5'])

        user_equity = st.number_input(label ='Enter the equity percentage of the mutual fund(0 to 100) based on this we debt percentage will be automatically calculated', min_value=0, max_value=100)

        user_debt = 100-user_equity

        risk_of_the_fund_user = st.multiselect('Select the rating of the fund', ['Very High', 'High', 'Moderately High', 'Moderate',
            'Low to Moderate', 'Moderately Low', 'Low'])

        type_of_fund  =  st.multiselect('Select the type of the fund', ['Equity', 'Other', 'Hybrid', 'Solution Oriented', 'Debt']) 

        one_year_returns_user =  st.number_input(label ='Enter the one year returns of the mutual fund', value  = -0.69)

        five_year_returns_user =  st.number_input(label ='Enter the five year returns of the mutual fund',value  = 20.19)

        submitted = st.form_submit_button('Submit')

        if submitted:

            le = preprocessing.LabelEncoder()
            le.classes_ = np.load('classes.npy',allow_pickle=True)

            user_rating = le.fit_transform(user_rating)
            type_of_fund = le.fit_transform(type_of_fund)
            risk_of_the_fund_user = le.fit_transform(risk_of_the_fund_user)

            with open('lst_transform.pkl', 'rb') as f:
                mynewlist = pickle.load(f)
           
            analysis = {

            'aum_funds_individual_lst':user_AUM/mynewlist[0],
            'nav_funds_individual_lst':user_NAV,
            'rating_of_funds_individual_lst':user_rating,
            'debt_per':user_debt/mynewlist[1],
            'equity_per':user_equity/mynewlist[3],
            'risk_of_the_fund':risk_of_the_fund_user,
            'type_of_fund':type_of_fund ,
            'one_year_returns':one_year_returns_user/mynewlist[2],
            'five_year_returns':five_year_returns_user/mynewlist[5],
            }

            prediction_tables = pd.DataFrame(analysis)   

            pickled_model = pickle.load(open('model_three_year_returns.pkl', 'rb'))
            prediction = pickled_model.predict(prediction_tables)


            if prediction <= 0:           
                st.metric(label="Three Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)+(one_year_returns_user/mynewlist[2])) + '%')
            else :
                st.metric(label="Three Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)-(one_year_returns_user/mynewlist[2])) + '%')
        


def Five_year_returns_predictions():
    st.subheader('Five year returns predictions')


    with st.form(key='my_form_five'):

        user_AUM = st.number_input(label ='Enter the AUM of the mutual fund')

        user_NAV = st.number_input(label ='Enter the NAV of the mutual fund')

        user_rating  = st.multiselect('Select the rating of the fund', ['1', '2', '3', '4','5'])

        user_equity = st.number_input(label ='Enter the equity percentage of the mutual fund(0 to 100) based on this we debt percentage will be automatically calculated', min_value=0, max_value=100)

        user_debt = 100-user_equity

        risk_of_the_fund_user = st.multiselect('Select the rating of the fund', ['Very High', 'High', 'Moderately High', 'Moderate',
            'Low to Moderate', 'Moderately Low', 'Low'])
        type_of_fund  =  st.multiselect('Select the type of the fund', ['Equity', 'Other', 'Hybrid', 'Solution Oriented', 'Debt']) 
    

        one_year_returns_user =  st.number_input(label ='Enter the one year returns of the mutual fund')

        three_year_returns_user =  st.number_input(label ='Enter the three year returns of the mutual fund')

        submitted = st.form_submit_button('Submit')

        if submitted:

            le = preprocessing.LabelEncoder()
            le.classes_ = np.load('classes.npy',allow_pickle=True)

            user_rating = le.fit_transform(user_rating)
            type_of_fund = le.fit_transform(type_of_fund)
            risk_of_the_fund_user = le.fit_transform(risk_of_the_fund_user)

            with open('lst_transform.pkl', 'rb') as f:
                mynewlist = pickle.load(f)
           
            analysis = {

            'aum_funds_individual_lst':user_AUM/mynewlist[0],
            'nav_funds_individual_lst':user_NAV,
            'rating_of_funds_individual_lst':user_rating,
            'debt_per':user_debt/mynewlist[1],
            'equity_per':user_equity/mynewlist[3],
            'risk_of_the_fund':risk_of_the_fund_user,
            'type_of_fund':type_of_fund ,
            'one_year_returns':one_year_returns_user/mynewlist[2],
            'three_year_returns':three_year_returns_user/mynewlist[4],
            }

            prediction_tables = pd.DataFrame(analysis)   

            pickled_model = pickle.load(open('model_five_year_returns.pkl', 'rb'))
            prediction = pickled_model.predict(prediction_tables)


            if prediction <= 0:           
                st.metric(label="Five Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)+(one_year_returns_user/mynewlist[2])) + '%')
            else :
                st.metric(label="Five Year returns", value = str(prediction[0]*100) + ' %',delta=str((prediction[0]*100)-(one_year_returns_user/mynewlist[2])) + '%')




        
page_names_to_funcs = {
    "Five year returns predictions": Five_year_returns_predictions,
    "Three year returns predictions": Three_year_returns_predictions,
    "One year returns predictions": One_year_returns_predictions,
    "Visualization":visualization

}



demo_name = st.sidebar.selectbox("Choose which page to view", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()




# df = pd.read_excel('cleaned_data.xlsx')

# df = df.drop(axis = 0, columns=['Unnamed: 0','minimum_funds_individual_lst'])

