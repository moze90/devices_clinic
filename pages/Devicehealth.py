import pickle
import numpy as np
import streamlit as st

option1=st.selectbox('Please enter the model you wish to use',('Device health classifier','Fail point regressor')
)
st.write('you selected the following model:',option1)
#gettting user input
#Cost		Count_WO					V3	age
Cost=st.number_input("enter the cost of the device")
Risk=st.number_input("enter the calculation risk number of the device")
Count_WO=st.number_input("enter the count of work order of the device")
Count_PM=st.number_input("enter the count of preventive maintenance of the device")
Meantime_PM=st.number_input("enter the average meantime between preventive maintenance the device")
V1=st.number_input("enter the the number of times pm done within29 days of their schedule")
V2=st.number_input("enter the the number of times pm done within60 days of their schedule")
V3=st.number_input("enter the the number of times pm done within90 days of their schedule")
age=st.number_input("enter the age of the device")
mylist=[Cost,Risk,Count_WO,Count_PM,Meantime_PM,V1,V2,V3,age]
print(mylist)
RUL_ana=5338
RUL_oxy=2247
RUL_patient=2857
#making input function to predict
with open('model_pickle','rb')as f:
    model_class=pickle.load(f)
def pred():
    input_as_np_array=np.asarray(mylist)
    print(input_as_np_array)
    input_data_reshaped=input_as_np_array.reshape(1,-1)
    predic_final=model_class.predict(input_data_reshaped)
    print(predic_final)
    if predic_final==0:
        st.write("this a Healthy device and you can continue using the same pm schedule and usage practices")
    else:
        st.write("this not a healthy device,please revise it pm activities and usage practices")
if (st.button("Get device status now"))== True:
    pred()
option2 = st.selectbox('please pick one of the two available devices',
                       ('Anesthesia', 'oxygen concentrator','patient monitor'))
if option2 == "Anesthesia":
    RUL1=RUL_ana - age
    st.write('Reamining useful life for this device is:', RUL1,'Days')
elif option2 == "oxygen concentrator":
    RUL2=RUL_oxy - age
    st.write('Reamining useful life for this device is', RUL2, 'days')
else:
    RUL3=RUL_patient-age
    st.write('Reamining useful life for this device is', RUL3, 'days')

