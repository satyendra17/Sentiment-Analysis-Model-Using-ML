import streamlit as st
import pickle
import time

#loading model

model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# creating title

st.title('Sentiment Analysis Model')

review = st.text_input('Enter your Review')

submit = st.button('Predict')

if submit:
     
     start = time.time()
     prediction = model.predict([review])

     end = time.time()

     st.write('Prediction time taken:' , round(end-start, 2 ))

     if prediction[0]=='positive':
           st.success('Positive Review')

     else: 
           st.warning ('Negative Review')