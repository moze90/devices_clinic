import pickle
import numpy as np
import streamlit as st

option1=st.selectbox('Please enter the model you wish to use',('Device health classifier','Fail point regressor')
)
st.write('you selected the following model:',option1)

#gettting user input
#Cost		Count_WO					V3	age
Count_wo=st.number_input("enter the count of work order of the device(will find it Count_Wo")
count_pm=st.number_input("enter the count of preventive maintenance of the device(will find it Count_pm")
meantime_pm=st.number_input("enter the average meantime between preventive maintenance the device")
wotime_diff=st.number_input("enter after how many days did the previous failure happend")
age=st.number_input("enter the age of the device")
meantime=st.number_input("enter the meantime between failures")
mylist=[Count_wo,meantime,count_pm,meantime_pm,wotime_diff,age]
print(mylist)
#making input function to predict
def pred1():
    global predic_final1
    input_as_np_array=np.asarray(mylist)
    print(input_as_np_array)
    input_data_reshaped=input_as_np_array.reshape(1,-1)
    predic_final1=model_class1.predict(input_data_reshaped)
    return predic_final1
with open('model_pickle_patientmonitor','rb')as f:
    model_class1=pickle.load(f)
if (st.button("Get device status now"))== True:
    pred1()
    st.write("the next failure is after",predic_final1)


