import streamlit as st
from textblob import TextBlob

st.title("Real-Time Sentiment Analysis")

text = st.text_input("Enter your text")

if text:

    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        st.success("Positive 😊")

    elif analysis.sentiment.polarity == 0:
        st.info("Neutral 😐")

    else:
        st.error("Negative 😡")