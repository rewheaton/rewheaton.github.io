import os
import glob
import streamlit as st
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB # Naive Bayes
from sklearn.linear_model import SGDClassifier # SVM
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Create list of options for dropdown:
cs = ["Naive Bayes","SVM"]

# Define a selectbox option:
classification_space = st.sidebar.selectbox("Pick a classification method:", cs)

# Write a few phrases to the app on the screen:
st.write("Results")
st.write('Dataset details here:')
st.write("Twenty Newsgroup dataset chosen. It contains over 20000 posts from newspapers and 20 different topics.")

trainData = fetch_20newsgroups(subset='train', shuffle=True)

if( "native_bayes_classificationPipeline" not in st.session_state):
    st.write("Training Naive Bayes...")
    st.session_state.native_bayes_classificationPipeline = Pipeline([('bow', CountVectorizer()),
                                            ('vector', TfidfTransformer()), 
                                            ('classifier ', MultinomialNB())])
    st.session_state.native_bayes_classificationPipeline = st.session_state.native_bayes_classificationPipeline.fit(trainData.data, trainData.target)

    st.write("Native Bayes classification pipeline created.")

if( "svm_classificationPipeline" not in st.session_state):
    st.write("Training SVM...")
    st.session_state.svm_classificationPipeline = Pipeline([('bow', CountVectorizer()), 
                                            ('vector', TfidfTransformer()), 
                                            ('classifier', SGDClassifier(loss='hinge', penalty ='l1', alpha=0.0005, l1_ratio=0.17))])

    st.session_state.svm_classificationPipeline = st.session_state.svm_classificationPipeline.fit(trainData.data,trainData.target)

    st.write("SVM classification pipeline created.")

# Create a button object:
if st.sidebar.button('Classify'):
    # Using a simple if statement, perform some task based on the selectbox options.
    # If the selectbox option is "Naive Bayes", then perform a Naive Bayes classifier.
    if classification_space == "Naive Bayes":
        st.write("Naive Bayes selected")
        
        test_set = fetch_20newsgroups(subset='test', shuffle=True)
        dataPrediction = st.session_state.native_bayes_classificationPipeline.predict(test_set.data)

        # Print to the application on the screen the results of the Naive Bayes classification:
        st.write("Accuracy of Naive Bayes Classification:")
        st.write(np.mean(dataPrediction == test_set.target))

    # If the selectbox option is "SVM", then perform a Support Vector Machine classifier.
    if classification_space == "SVM":
        trainData = fetch_20newsgroups(subset='train', shuffle = True)
        st.write("SVM selected")
        
        test_set = fetch_20newsgroups(subset='test', shuffle=True)
        dataPrediction = st.session_state.svm_classificationPipeline.predict (test_set.data)
        # Print to the application on the screen the results of the SVM classification:
        st.write("Accuracy of SVM Classification:")
        st.write(np.mean(dataPrediction == test_set.target))

