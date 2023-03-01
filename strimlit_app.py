import streamlit as st
import pickle

st.text('welcome to SoftPro medical devices Clinic')
st.text('We have two main models :1-device healt classiffier and Next Fail point regressor')
st.text('please pick which model you want to work with')
option1 = st.selectbox('please pick one of the two available models',
                       ('Device health calssification', 'FAIL POINT REGRESSOR'))

if option1 == "Device health calssification":
    st.write("you are viewing health model")
else:
    st.write("you are viewing next fail regression")

option = st.selectbox('Get data per devices type', ('Anathesia', 'Patient monitor', 'Oxygen concentrators'))
st.write('You selected:', option)
st.write("this is the number of"+'' + option + ''+"available for the modeling phase")
if (option == "Anathesia"):
    st.write()
elif (option == "Patient monitor"):
    st.write()

