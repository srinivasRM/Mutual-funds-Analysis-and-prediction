<h1 align="center"> Mutual Funds Analysis and Prediction</h1>

Hey guys! My name is R M Srinivas. In this project I have performed analysis and prediction on 1,3,and 5 year returns on 1064 mutual funds in India. 
I have scraped data from a website which is the most visited website for mutual fund investments.I have tested regression models linear model,SGD Regressor ,
Random Forest Regressor,Decision Tree Regressor,Ridge,MLP Regressor and linear model (Lasso).After which I have selected the best perorming model and performed 
Hyper parameter tuning and then deployed an interactive application which can generate the visualization and send an email with the visualization to the users
email address.

<h2 align="center">

Here is a gif of the application :video_camera: 

</h2>

![Animation](https://user-images.githubusercontent.com/94186999/180741669-bd86a3bf-15ec-49a0-9a54-7bdc20d265db.gif)

# ETL

Extraction(https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/scraper%20and%20extraction.py): - In the current file I used Beautiful soup to 
extract data from the most visited site to study/analyse/invest into Mutual funds. Extracted 20 columns from the website with 1064 mutual funds. I tried extract in a way such that 
there should not be much data cleaning afterwards. After which I saved the file as raw_data.xlsx.

Transform(https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/Tranformation.py): - As the data did not have much steps to clean I have cleaned the raw data that 
was taken in the above step and removed few columns that had more than 30% missing values(np.nan). Changed the column with the funds AUM in cr to float. Saved the file as cleaned_data.xlsx

Load(https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/data_storage.py): - In this file I loaded/uploaded the data to Heroku server for storage of the data and I used Postgresql
to send and save the data. Evertime the current file runs it takes the updated data drops the existing column if it exists and then add the updated table/data to the server. 

# EDA(Exploratory data analysis) 

Go through the following links for individual ipynb files. 

5 year retutns models testing - >

https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/Model%20testing%20for%205%20year%20analysis.ipynb

3 year retutns models testing - >

https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/Model%20testing%20for%203%20year%20analysis.ipynb

1 year retutns models testing - >

https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/Model%20testing%20for%201%20year%20analysis.ipynb

Let's first understand the relation of our target variable(returns over the perior of 1,3 and 5 years) with the remaining variables. Let's first understand some basic definitions. 
AUM or Assets Under Management is the total funds that a mutual fund scheme holds.

What does NAV mean?
The performance of a particular scheme of a Mutual Fund is denoted 
by Net Asset Value (NAV). In simple words, NAV is the market value 
of the securities held by the scheme. Mutual Funds invest the money
collected from investors in securities markets. 

Risk of the fund 
Mutual Fund Schemes are not guaranteed or assured return products. 
Investment in Mutual Fund Units involves investment risks such as 
trading volumes, settlement risk, liquidity risk, default risk 
including the possible loss of principal all of this is 
considered and rated accordingly. 

Minium Investment
Its the minimum amount limit for investing in a mutual fund. 

Type of the fund. 
There are different funds based on there diversification in the 
investments they are classified. Equity fund, Debt fund , hybrid fund, 
Solution based funds, etc... 

## Outlier analysis and treatment. 
Here are few basic information regarding the columns using describe function. We can see that there outliers in few columns lets go ahead and investigate those columns and treat them. 

![5 YEAR describe](https://user-images.githubusercontent.com/94186999/180749164-e95a7015-8d28-41ad-bfa5-47696225ecef.JPG)

## Here is box plot and dist plot of the AUM column before outlier treatment.  
![box plot of aum 5 year](https://user-images.githubusercontent.com/94186999/180749174-4de5ba8e-3130-445a-a752-78e5813b6155.JPG)

## Here is box plot and dist plot of the debt percentage column before outlier treatment.  
![box plot and dist plot dep_percentage 5 year](https://user-images.githubusercontent.com/94186999/180749316-2a200250-42e0-4687-b376-429ce94b5e8a.JPG)

## Here is box plot and dist plot of the 5 year returns column before outlier treatment.  
![box plot for 5 year returns](https://user-images.githubusercontent.com/94186999/180749331-3783b4f3-995e-4631-90b0-bfa6331679be.JPG)


## Here is box plot and dist plot of the equity percentage column before outlier treatment.  
![box plot for equity percentage](https://user-images.githubusercontent.com/94186999/180749341-007644a6-25c8-422f-badc-9edf7235995c.JPG)

## Here is box plot and dist plot of the  3 year returns before outlier treatment.  
![box plot for 3 year returns](https://user-images.githubusercontent.com/94186999/180749370-444612d3-9c35-46a9-87f5-da5b36728f36.JPG)

## Here is box plot and dist plot of the  3 year returns before outlier treatment.  
![after treatment of outlieres aum](https://user-images.githubusercontent.com/94186999/180749404-293668be-01e1-4fb9-9ae8-aa519d1799bf.JPG)

## Treatment of outliers 
Tried removing the values greater than 0.85 with mean, median and normalized each column and compared the results which I have documented as a in bottom section of the table. 

## Here is box plot and dist plot of the AUM column after outlier treatment.  
![after treatment 2](https://user-images.githubusercontent.com/94186999/180749440-6279034c-354c-44ae-981f-b591a13d87ce.JPG)

## Here is box plot and dist plot of the debt percentage column after outlier treatment.  
![after treatment](https://user-images.githubusercontent.com/94186999/180749459-b9fba7b9-a53a-4c03-baf0-fa25b7b1e537.JPG)

## Here is box plot and dist plot of the 5 year returns column before after treatment.   
![after treatment 3](https://user-images.githubusercontent.com/94186999/180749472-6c2714d0-8a3b-4fad-b7e7-91739a9b616d.JPG)

## Here is box plot and dist plot of the equity percentage column after outlier treatment.  
![after treatment 4](https://user-images.githubusercontent.com/94186999/180749486-6b5d3b4c-6023-4834-8b0b-ae9c55125ec8.JPG)

## Here is box plot and dist plot of the  3 year returns after outlier treatment.  
![after treatment 5](https://user-images.githubusercontent.com/94186999/180749505-4e4bebd0-cbf5-477a-abbb-88a9dd817ce5.JPG)

## Here is the correlation matrix of the data after outlier treatment
![correlation matrix 5 year](https://user-images.githubusercontent.com/94186999/180749510-2bd84341-056f-440c-a718-1985d5d4bc97.JPG)

## Here is an table which shows us testing scores of various models on the 5 Year returns target variable.
![5 year outlier table](https://user-images.githubusercontent.com/94186999/180749527-00d982bc-907b-4d1f-bcb4-e7437b00af43.JPG)

## Here is an table which shows us testing scores of various models on the 3 Year returns target variable.
![3 year outlier anyaluis results](https://user-images.githubusercontent.com/94186999/180749538-beed151d-a7fc-46e8-9ebf-a0ffbebc1fdd.JPG)

## Here is an table which shows us testing scores of various models on the 1 Year returns target variable.
![1 year outlier anaylis and report](https://user-images.githubusercontent.com/94186999/180749542-97cd36fb-f1c8-4cb8-8c24-4fbd5f9616f0.JPG)

In of the above images for 1,3,5 retunrns model testing, the best model according to the scored obtained is the random forst regressor, and performed Hyper parameter tuning 
individually for the best results. After pickled the models for running it in the Deployment phase of the project. 

Here is the final graphs Individually after hyper parameter optimization and feature importance graph.

## Graphs for 1 year precitions 

![1 year model after hyper parameter](https://user-images.githubusercontent.com/94186999/180754863-16eb31c8-f2c0-4a4c-bdfd-9c9e78f05fed.JPG)

![feature importance one year](https://user-images.githubusercontent.com/94186999/180754870-9fcaf830-a7ef-4c93-a8e8-297e48b81295.JPG)

## Graphs for 3 year precitions 

![3 year predictions](https://user-images.githubusercontent.com/94186999/180754813-f8fb44b5-1f30-4d85-ba6a-a84888662141.JPG)

![feature importance 3 year](https://user-images.githubusercontent.com/94186999/180754824-5f014829-1ca6-481c-915d-490ef433e117.JPG)

## Graphs for 5 year precitions 

![5 year predictions](https://user-images.githubusercontent.com/94186999/180754778-dc65b805-b8e5-4ab9-ab55-d2177766eb5f.JPG)

![5 year returnis impportance](https://user-images.githubusercontent.com/94186999/180754789-41696706-143a-4ab1-8813-657b7ca7bb09.JPG)


## Front end application(https://github.com/srinivasRM/Mutual-funds-Analysis-and-prediction/blob/main/Deployment.py)
Using Streamlit Created the following application 
![Animation](https://user-images.githubusercontent.com/94186999/180755420-6e0a29f2-edf9-4ff8-a394-19623e67f607.gif)

The above application has a sidebar that can be accessed for moving through the 5 different pages. Deinition page has the basic information about the various fund related information. 
After which there are series of 3 pages which can predict the returns based on inputs provided. In the back end after opening each page the respective models saved in pickle format is opened 
and the user inputs are normalized and converted for getting the prediction. The last page will have all the visualization and analysis with description. Created a requirements.txt for future deployment 
of the project onto a AWS or Heroku Cloud. 


Let me know if you have any suggestions. You can contact me on this email - rmsrinivas199627@gmail.com




