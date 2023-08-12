import streamlit as st
import pandas as pd
gender_list=['Male','Female']
st.radio('gender',gender_list)
st.slider('age',0,130,16)
st.text_area('Topic','Please enter your title')
st.text_area('Sign','Please enter your Zodiac Sign')
st.date_input('Date')
st.text_area('Blog content','Please enter your context')
overall_seo_score=5
st.subheader('Your Report: ')
if overall_seo_score >= 7.5:
    st.markdown("Execellent")
elif overall_seo_score >= 5:
    st.markdown("Good")
else:
    st.markdown("Needs Improvement")
st.title(overall_seo_score)
