added link to open model directly 


[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://satyendra17-sentiment-analysis-model-using-ml-app-s6nueh.streamlit.app/)


Sentiment Analysis with Machine Learning 
This repository contains code for sentiment analysis using various machine learning models. The sentiment analysis is performed on the IMDB dataset, and the following models are implemented:  Linear Support Vector Classifier (SVC) Logistic Regression Multinomial Naive Bayes Random Forest 
Getting Started 
Prerequisites 
Make sure you have the required Python libraries installed. You can install them using the following command:  bash pip install spacy beautifulsoup4 textblob mlxtend python -m spacy download en_core_web_sm pip install git+https://github.com/satyendra17/preprocess_functions.git --upgrade --force-reinstall 

Installation 
Clone the repository:  bash git clone https://github.com/your-username/your-repo.git cd your-repo Install the required Python packages:  bash Copy code pip install -r requirements.txt Usage Run the Jupyter notebook or Python script to perform sentiment analysis and train the models.  bash 
python sentiment_analysis_script.py Models The trained models are saved in the repository:  LinearSVC: sentiment_analysis.pkl 

Results 
Detailed results, including accuracy and confusion matrices, are available in the notebook.  Contributor Satyendra Prakash  License This project is licensed under the MIT License - see the LICENSE.md file for details.  
