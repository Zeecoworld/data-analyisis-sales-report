import os
import pandas as pd
import streamlit as st
import plotly.express as px

path = os.path.dirname(__file__)
myfile = path+'/Annual-sales-report-2020.csv'


st.set_page_config(page_title='SALES ANALYSIS REPORT 2020 FOR COMPANY 2020')

st.header('SALES REPORT OF A COMPANY ABC IN YEAR 2020')

st.subheader('DATA ANALYSIS ON A CLIENT PROJECT')

# st.subheader('UPLOAD YOUR DATASET')

# data_file = st.file_uploader("UPLOAD DATASET",type=["csv"])

# if data_file is not None:
#     file_details = {"filename":data_file.name,"filetype": data_file.type,"filesize": data_file.size}
#     st.write(file_details)
#     df = pd.read_csv(data_file)
#     st.dataframe(df)
    

DATA = 'Annual-sales-report-2020.csv'

df = pd.read_csv(myfile)

st.dataframe(df)

df_month = df["Month"]

df_details = df.iloc[:, 1:]

st.dataframe(df_details)

pie_chart = px.pie(df, title="Visual Report of Sales By Month",values="Sales(naira)",names="Month")
st.plotly_chart(pie_chart)



pie_chart = px.pie(df, title="Visual Report of Loss By Month",values="Loss(naira)",names="Month")
st.plotly_chart(pie_chart)


st.subheader('Finally, Which month has the highest and lowest Profit Margins???🤔')


df_detail_by_describe = df_details.describe().loc['min':'max']

st.dataframe(df_detail_by_describe)

st.subheader('Obviously, The month with Highest and lowest Profit Margins are: DECEMBER and FEBURARY')

    # st.subheader('Obviously, The month with Highest and lowest Profit Margins are: Feburary and December')


    # st.subheader(" \'GENEROSITY BREEDS HAPPINESS\' ")
# else:
#     pass
