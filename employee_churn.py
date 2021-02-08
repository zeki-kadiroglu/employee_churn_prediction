# first we imported libraries we need
import streamlit as st
import pickle
import pandas as pd
# Create a app title with title method

st.title('Employee Churn Prediction')
# We called back our models created before
model1 =pickle.load(open("rfc_model","rb"))
model2= pickle.load(open("clf_model","rb"))


# We use selectbox method and append our models to give a choice clients
models = st.selectbox("Select Model",("Random Forest","Gradient Descent"))

# And specified a condition if users select Random forest use random forest model else use Xgboost model.
if models == "Random Forest":
    model = model2
elif models =="Gradient Descent":
    model = model1

    

# We created selectbox for categorical columns and used slider numerical values ,specified range and step 
salary = st.selectbox('What is your employee salary level',(1,2,3))
satiscfaction_level = st.slider('What is your employee satisfaction rate',0.0,1.0,step=0.01)
time_spend_company= st.selectbox('What is your employee time spend in company', ('1','2','3','4','5+'))
departments = st.selectbox('What is your employee department?', ('IT','RandD','accounting','hr','management','marketing','product_mng','sales','support','technical'))


# in order to recieved client inputs appended these inputs (created above) into dictionary as we mentioned before. And We returned into dataframe.

my_dict = {'salary':salary,'satiscfaction_level':satiscfaction_level,'time_spend_company':time_spend_company
           ,'departments':departments}

df = pd.DataFrame.from_dict([my_dict])
columns = ['salary','satisfaction_level','time_spend_company','IT','RandD','accounting','hr','management','marketing'
           ,'product_mng','sales','support','technical']

# And appended column names into column list. We need columns to use with reindex method as we mentioned before.
df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

# We append all columns in the user input dataframe and reindex method just received relevant user inputs , and return other columns from nan to zero with fill_value=0 parameter.
# And now we can predict
prediction = model.predict(df)
predict = st.button('Guess What') 
# Success method demonstrate our prediction in a green square

if predict:
    if int(prediction[0])==0:
        st.success("Loyal employee's will remain in the company")
        
    elif int(prediction[0])==1:
        st.success("employee's will left from the company in future")
    
