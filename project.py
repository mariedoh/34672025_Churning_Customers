import streamlit as st
import pandas as pd
import pickle

with open("mod_creator(1).pkl", "rb") as c_model:
    create_model = pickle.load(c_model)
with open("modell.pkl", "rb") as file:
    model = pickle.load(file)

features = ['TotalCharges', 'MonthlyCharges', 'Contract', 'PaymentMethod', 'OnlineSecurity', 'gender',
            'PaperlessBilling', 'Partner', 'OnlineBackup', 'TechSupport', 'Dependents', 'MultipleLines',
            'DeviceProtection', 'InternetService', 'StreamingMovies', 'StreamingTV', 'tenure', 'SeniorCitizen', 'PhoneService']

st.set_page_config(
    page_title="CUSTOMER CHURNING",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.header("Welcome Fretting StoreOwners")
st.subheader("Calculate the Probability of Your Customer Churning", divider="violet")
permissionToProceed = st.text_input(
    "Disclaimer: This will require you to enter sensitive information. Enter yes only if you wish to proceed.")

if permissionToProceed.lower() == "yes":
    total_charge = st.number_input("What is this customer's total charge for this year?")
    monthly_charge = st.number_input("What is this customer's monthly charge?")
    contract = st.select_slider("What type of contract does this customer have? Enter 0 for monthly, 1 for yearly.",
                                [0, 1])
    payment_m = st.select_slider(
        "How does this customer usually pay? Enter 0 for bank transfer, 1 for credit card, 2 for electronic check, 3 for mailed check",
        [0, 1, 2, 3])
    Osecurity = st.select_slider(
        "Do they have online Security? Enter 0 for no,1 for if they don't have phone service, and 2 for yes", [0, 1, 2])
    gender = st.select_slider("What is your gender? Enter 0 for female, 1 for male", [0, 1])
    paperlessBilling = st.select_slider("Are they billed paperlessly? Enter 0 for no, 1 for Yes.", [0, 1])
    partner = st.select_slider("Do they have partners? 0: No, 1: Yes", [0, 1])
    onlineBack = st.select_slider(
        "Do they have online backups? Enter 0 for No and 1 if they dont have phones, 2 for Yes ", [0, 1, 2])
    techS = st.select_slider(
        "Do you offer them tech support? Enter 0 for No, 1 if they don't have internet service, and 2 for yes.",
        [0, 1, 2])
    dependent = st.select_slider("Do they have dependents? Enter 0 for no, 1 for yes", [0, 1])
    multipleLines = st.select_slider(
        "Do they have multiple phone lines? Enter 0 for no, 1 if they don't have phone service, and 2 for yes.",
        [0, 1, 2])
    devicePro = st.select_slider(
        "Do they have device protection? Enter 0 for no, 1 if they don't have internet service, 2 for yes ",
        [0, 1, 2])
    internetService = st.select_slider("Do they have internet service? O for no, 1 for yes.", [0, 1])
    streamMov = st.select_slider("Do they stream movies? 0 for no, 1 if no internet service 2 for yes.", [0, 1, 2])
    streamTV = st.select_slider(
        "Do they stream television? 0 for no,1 if no internet service and 2 for yes", [0, 1, 2])
    tenure = st.number_input("How long have they stayed with you? (in years)")
    senior = st.slider("How old are they?", 0, 100)
    phoneService = st.select_slider("Do they have phone service? 0 for no, 1 for yes.", [0, 1])
    user_input = [total_charge, monthly_charge, contract, payment_m, Osecurity, gender, paperlessBilling, partner,
                  onlineBack, techS, dependent, multipleLines,
                  devicePro, internetService, streamMov, streamTV, tenure, senior, phoneService]
    button = st.button("Predict")
    if button:
        use = pd.DataFrame([user_input], columns=features)
        prediction = model.predict(use.values.reshape(1, -1))[0]
        if prediction == 0:
            st.write("This customer will not churn")
        else:
            st.write("This customer will churn.")
        

