import streamlit as st
import joblib
st.title('Loan Approval process automation')
model= joblib.load('loan_data1.joblib')
gender= st.number_input('Enter gender (M:0,F:1)',min_value=0,max_value=1,step=1)
married= st.number_input('Enter marital status (M:1,UM:0)',min_value=0,max_value=1,step=1)
income= st.number_input('Enter applicant income in thousands')
la=st.number_input('Enter loan amount in thousands')
if st.button('Predict Approval'):
    prediction=model.predict([[gender,married,income,la]])
    if prediction[0]=='Y':
        st.success('Loan Approved')
    else:
        st.error('Loan Rejected')
