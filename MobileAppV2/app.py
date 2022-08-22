## import libraries
import pandas as pd
import streamlit as st
import pickle
import numpy as np

model=pickle.load(open(r"MobileApp/model.pkl",'rb'))     ## Load pickeled ml model

## Main Function
def main():
    """ main() contains all UI structure elements; getting and storing user data can be done within it"""
    st.title("Term Deposit Prediction")                                                                              ## Title/main heading
    st.image(r"MobileApp/bank.png", caption="Know your customers",use_column_width=True) ## image import
    st.write("""## Is the customer likely to subscriber term deposit?""")                                                    ## Sub heading

    ## Side Bar Configurations
    # st.sidebar.header("More Details:")
    # st.sidebar.markdown("[For More facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")
    # st.sidebar.markdown("[and here](https://titanicfacts.net/titanic-survivors/)")
    st.title("-----          Type in customer info          -----")

    ## Framing UI Structure
    age = st.slider("Enter Age :", 1, 90, 30)
    Age = age/100                                                                  # slider for user input(ranges from 1 to 75 & default 30)

    # fare = st.slider("Fare (in 1912 $) :", 15, 500, 40)                                                        # slider for user input(ranges from 15 to 500 & default 40)

    # SibSp = st.selectbox("How many Siblings or spouses are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box

    # Parch = st.selectbox("How many Parents or children are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box

    marital = st.selectbox("Select Marital Status:", ["married","single", "divorced","unknown"])                         # select box for gender[Male|Female]
    if (marital == "married"):                                                             # selected gender changes to [Male:0 Female:1]
        Marital=0/3
    elif (marital == "single"): 
        Marital=1/3
    elif (marital == "divorced"): 
        Marital=2/3             
    else:
        Marital=3/3
    
    default = st.selectbox("Have you ever been default?:", ["yes","no","unknown"])                   
    if (default == "yes"):                                                             
        Default = 1/2
    elif (default == "no"):
        Default = 0/2       
    else:
        Default = -1/2        

    housing = st.selectbox("Do you own any property/ies?:", ["yes","no","unknown"])                   
    if (housing == "yes"):                                                             
        Housing = 1/2
    elif (housing == "no"):                                                             
        Housing = 0/2        
    else:
        Housing = -1/2         

    loan = st.selectbox("Do you in debt or have any loan?:", ["yes","no","unknown"])                   
    if (loan == "yes"):                                                             
        Loan = 1/2  
    elif (loan == "no"):                                                             
        Loan = 0/2      
    else:
        Loan = -1/2  

    poutcome = st.selectbox("previous outcome?:", ["success","failure","nonexistent"])  
    if (poutcome == "success"):                                                             
        Poutcome = 2/2 
    elif (poutcome == "failure"):                                                             
        Poutcome = 0/2      
    else:
        Poutcome = 1/2

    job = st.selectbox("What is your job?:", ["blue collar","white collar","not working", "other"])                   
    if (job == "blue collar"):                                                             
        Job = 3/3  
    elif (job == "white collar"):                                                             
        Job = 2/3    
    elif (job == "not working"):                                                             
        Job = 1/3     
    else:
        Job = 0/3

    education = st.selectbox("What is your education level?:", ["post high school","high school","pre high school", "other"])                   
    if (education == "post high school"):                                                             
        Edu = 3/3  
    elif (education == "high school"):                                                             
        Edu = 2/3    
    elif (education == "pre high school"):                                                             
        Edu = 1/3     
    else:
        Edu = 0/3
    
    #numeric features
    campaign = st.slider("campaign :", 1, 56, 1) 
    CAM = (campaign - 1)/55

    pdays = st.slider("pdays :", 0, 999, 999) 
    PD = pdays/1000  

    previous = st.slider("previous :", 0, 7, 0)
    PRE = previous/7 

    emp_rate = st.slider("emp_var_rate :", -3.5, 2.5, 1.4)
    EM = emp_rate/6

    price_idx = st.slider("price idx :", 92.000, 94.000, 93.994)
    PR = (price_idx-92)/2  

    conf_idx = st.slider("conf idx :", -60.00, -30.00, -36.4)
    CON = (conf_idx + 60)/30

    eurobor3m =   st.slider("eurobor3m :", 0.000, 5.000, 4.857)
    EU3 = eurobor3m / 5

    nr_employed = st.slider("nr_employed :", 4963, 5228, 5228)
    NR = (nr_employed-4963) / (5228-4963)

    # Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])                        # Select box for passenger-class

    # boarded_location = st.selectbox("Boarded Location:", ["Southampton","Cherbourg","Queenstown"]) ## Select Box for Boarding Location
    # Embarked_C,Embarked_Q,Embarked_S=0,0,0                     # initial values are 0
    # # As we encoded these using one-hot-encode im ml model; so if 'Q' selected value is C=0,Q=1;S=0 , if 'S' selected value is C=0,Q=0;S=1 likewise
    # if boarded_location == "Queenstown":
    #     Embarked_Q=1
    # elif boarded_location == "Southampton":
    #     Embarked_S=1
    # else:
    #     Embarked_C=1

    ## Getting & Framing Data: Collecting user-input into dictionary
    data={"age":Age,"marital":Marital,"default":Default,"housing":Housing,"loan":Loan,"campaign":CAM,"pdays":PD,"previous":PRE,"poutcome":Poutcome, 
    "emp.var.rate": EM, "cons.price.idx":PR, "cons.conf.idx":CON, "euribor3m": EU3, "nr.employed": NR, "edu_new": Edu, "job_new": Job}

    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()

## Prediction:
if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(data)                                                        ## prediction of user-input
    proba=model.predict_proba(data)                                                   ## probabilty prediction of user-input
    #st.success('The output is {}'.format(result))

    if result == 1:
        st.write("***This customer is likely to subscribe....*** **You should reach out**")
        st.image("MobileAppV2/call.jpg", use_column_width=True)
        st.write("**Subscription Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("***This customer is probably not interested...***")
        st.image("MobileAppV2/notcall.JPG", use_column_width=True)
        st.write("**Subscription Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))

# ## Working Button:
# if st.button("Working"):                                                      # creating Working button, which gets some survival tips & info.
#     st.write("""# How's prediction Working :- Insider Survival Facts and Tips: 
#              - Only about `32%` of passengers survived In this Accident\n
#              - Ticket price:
#                     1st-class: $150-$435 ; 2nd-class: $60 ; 3rd-class: $15-$40\n
#              - About Family Factor:
#                 If You Boarded with atleast one family member `51%` Survival rate
#                """)
#     st.image(r"gr.PNG")

## Author Info.
if st.button("Author"):
    st.write("## @ Shawn")
