import streamlit as st
import pickle
import time
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(current_directory, 'sentiment_analysis.pkl')

# Load model
try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    print(f"Error loading the model: {e}")
    st.error(f"Error loading the model: {e}")

# Creating title
st.title('Sentiment Analysis Model')

# User input
review = st.text_input('Enter your Review')

# Prediction button
submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([review])
    end = time.time()

    st.write('Prediction time taken:', round(end - start, 2))

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')
