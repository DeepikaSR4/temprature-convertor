import streamlit as st
st.title("Temprature Convertor")
option = st.radio("Select an option",('Celsius to Fahrenheit','Fahreheit to Celsius'))
temp= st.number_input("Enter the temprature\n")

if(option=="Celsius to Fahrenheit"):
    convertedtemp = (temp*1.8) + 32
    st.write("\nConverted temprature " + str(convertedtemp) + " Fahrenheit")
else:
    convertedtemp = (temp-32)*(5/9)
    st.write("\nConverted temprature " + str(convertedtemp) + " Celsius")
